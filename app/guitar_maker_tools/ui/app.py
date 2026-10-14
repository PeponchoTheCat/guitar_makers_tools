"""Textual application for fretboard calculations."""

from decimal import Decimal

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, DataTable, Footer, Header, Input, Label, Select, Static

from ..calculations.fretboard import (
    FretMeasurement,
    calculate_fretboard,
    calculate_scale_from_fret_position,
)
from ..exporters import (
    format_millimetres,
    fretboard_to_csv,
    fretboard_to_text,
    write_export,
)
from ..presets import SCALE_PRESETS


class GuitarMakerApp(App[None]):
    """Interactive equal-temperament fret calculator."""

    TITLE = "Guitar Maker Tools"
    SUB_TITLE = "Theoretical equal-temperament fret positions"
    BINDINGS = [("q", "quit", "Quit")]

    CSS = """
    Screen { layout: vertical; }
    #forms { height: 15; }
    .panel { width: 1fr; margin: 0 1; padding: 0 1; border: round $primary; }
    .panel Input, .panel Select { margin-bottom: 0; }
    #results { height: 1fr; margin: 0 1; }
    #export { height: auto; margin: 0 1; }
    #export-path { width: 1fr; }
    #export-format { width: 12; }
    #inverse-result { margin-top: 0; }
    """

    def __init__(self) -> None:
        super().__init__()
        self.measurements: tuple[FretMeasurement, ...] = ()

    def compose(self) -> ComposeResult:
        preset_options = [("Custom", "custom")] + [
            (preset.name, str(preset.scale_mm)) for preset in SCALE_PRESETS
        ]
        yield Header()
        with Horizontal(id="forms"):
            with Vertical(classes="panel"):
                yield Label("Fret calculator")
                yield Select(preset_options, value="custom", id="scale-preset")
                yield Input(placeholder="Scale length (mm)", id="scale-input")
                yield Input(placeholder="Number of frets", id="fret-count-input")
                yield Button("Calculate frets", id="calculate-frets", variant="primary")
            with Vertical(classes="panel"):
                yield Label("Inverse scale calculator")
                yield Input(placeholder="Fret number", id="inverse-fret-input")
                yield Input(placeholder="Distance from nut (mm)", id="inverse-distance-input")
                yield Button("Calculate scale", id="calculate-inverse")
                yield Static("", id="inverse-result")
        yield DataTable(id="results")
        with Horizontal(id="export"):
            yield Input(placeholder="Export path", id="export-path")
            yield Select(
                [("CSV", "csv"), ("Text", "text")],
                value="csv",
                id="export-format",
            )
            yield Button("Export", id="export-button")
            yield Button("Quit", id="quit", variant="error")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#results", DataTable)
        table.add_columns(
            "Fret",
            "Distance from nut (mm)",
            "Previous spacing (mm)",
            "Residual length (mm)",
        )

    def on_select_changed(self, event: Select.Changed) -> None:
        if event.select.id != "scale-preset" or event.value == "custom":
            return
        self.query_one("#scale-input", Input).value = str(event.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        handlers = {
            "calculate-frets": self._calculate_frets,
            "calculate-inverse": self._calculate_inverse_scale,
            "export-button": self._export_selected_format,
            "quit": self.action_quit,
        }
        handler = handlers.get(event.button.id)
        if handler is not None:
            handler()

    def action_quit(self) -> None:
        """Close the application."""
        self.exit()

    def _calculate_frets(self) -> None:
        try:
            scale = self.query_one("#scale-input", Input).value
            fret_count = int(self.query_one("#fret-count-input", Input).value)
            self.measurements = calculate_fretboard(scale, fret_count)
        except ValueError as error:
            self.notify(str(error), severity="error")
            return

        table = self.query_one("#results", DataTable)
        table.clear()
        for measurement in self.measurements:
            values = (
                str(measurement.fret_number),
                format_millimetres(measurement.distance_from_nut_mm),
                format_millimetres(measurement.previous_spacing_mm),
                format_millimetres(measurement.residual_length_mm),
            )
            style = {
                12: "bold bright_yellow",
                14: "bold bright_magenta",
            }.get(measurement.fret_number)
            table.add_row(
                *(Text(value, style=style) if style else value for value in values)
            )
        self.notify(f"Calculated {len(self.measurements)} fret positions.")

    def _calculate_inverse_scale(self) -> None:
        try:
            fret_number = int(self.query_one("#inverse-fret-input", Input).value)
            distance = self.query_one("#inverse-distance-input", Input).value
            scale = calculate_scale_from_fret_position(distance, fret_number)
        except ValueError as error:
            self.notify(str(error), severity="error")
            return

        self.query_one("#inverse-result", Static).update(
            f"Theoretical scale: {format_millimetres(scale)} mm"
        )

    def _export_selected_format(self) -> None:
        """Export the current table using the selected format."""
        format_name = self.query_one("#export-format", Select).value
        if not isinstance(format_name, str):
            self.notify("Select an export format.", severity="error")
            return
        self._export(format_name)

    def _export(self, format_name: str) -> None:
        if not self.measurements:
            self.notify("Calculate fret positions before exporting.", severity="error")
            return

        path = self.query_one("#export-path", Input).value.strip()
        if not path:
            self.notify("Enter an export path.", severity="error")
            return

        content = (
            fretboard_to_csv(self.measurements)
            if format_name == "csv"
            else fretboard_to_text(self.measurements)
        )
        try:
            destination = write_export(path, content)
        except (OSError, ValueError) as error:
            self.notify(f"Export failed: {error}", severity="error")
            return
        self.notify(f"Exported {format_name.upper()} to {destination}.")
