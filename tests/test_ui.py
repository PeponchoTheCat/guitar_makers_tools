from pathlib import Path

import pytest
from rich.text import Text
from textual.coordinate import Coordinate
from textual.widgets import DataTable, Input, Select, Static

from guitar_maker_tools.ui.app import GuitarMakerApp


def test_quit_action_exits_the_application(monkeypatch: pytest.MonkeyPatch) -> None:
    app = GuitarMakerApp()
    exited = False

    def record_exit() -> None:
        nonlocal exited
        exited = True

    monkeypatch.setattr(app, "exit", record_exit)

    app.action_quit()

    assert exited


@pytest.mark.asyncio
async def test_fret_calculator_populates_table() -> None:
    app = GuitarMakerApp()

    async with app.run_test() as pilot:
        app.query_one("#scale-input", Input).value = "647.7"
        app.query_one("#fret-count-input", Input).value = "12"
        await pilot.click("#calculate-frets")

        assert app.query_one("#results", DataTable).row_count == 12


@pytest.mark.asyncio
async def test_results_table_is_visible_in_a_standard_terminal() -> None:
    app = GuitarMakerApp()

    async with app.run_test(size=(80, 24)):
        calculate_button = app.query_one("#calculate-frets")
        table = app.query_one("#results", DataTable)

        assert calculate_button.region.bottom <= app.query_one("#forms").region.bottom
        assert table.region.height >= 2
        assert table.region.bottom <= app.screen.region.bottom - 1


@pytest.mark.asyncio
async def test_export_controls_are_visible_in_a_standard_terminal() -> None:
    app = GuitarMakerApp()

    async with app.run_test(size=(80, 24)):
        export = app.query_one("#export")
        for selector in ("#export-path", "#export-format", "#export-button", "#quit"):
            control = app.query_one(selector)
            assert control.region.right <= export.region.right
            assert control.region.bottom <= app.screen.region.bottom - 1


@pytest.mark.asyncio
async def test_twelfth_and_fourteenth_fret_rows_are_colored() -> None:
    app = GuitarMakerApp()

    async with app.run_test() as pilot:
        app.query_one("#scale-input", Input).value = "647.7"
        app.query_one("#fret-count-input", Input).value = "14"
        await pilot.click("#calculate-frets")

        twelfth = app.query_one("#results", DataTable).get_cell_at(Coordinate(11, 0))
        fourteenth = app.query_one("#results", DataTable).get_cell_at(Coordinate(13, 0))

        assert isinstance(twelfth, Text)
        assert isinstance(fourteenth, Text)
        assert str(twelfth.style) == "bold bright_yellow"
        assert str(fourteenth.style) == "bold bright_magenta"


@pytest.mark.asyncio
async def test_inverse_calculator_displays_scale() -> None:
    app = GuitarMakerApp()

    async with app.run_test() as pilot:
        app.query_one("#inverse-fret-input", Input).value = "12"
        app.query_one("#inverse-distance-input", Input).value = "323.85"
        await pilot.click("#calculate-inverse")

        assert "647.700 mm" in str(app.query_one("#inverse-result", Static).render())


@pytest.mark.asyncio
async def test_csv_export_writes_the_current_fret_table(tmp_path: Path) -> None:
    app = GuitarMakerApp()
    destination = tmp_path / "frets.csv"

    async with app.run_test() as pilot:
        app.query_one("#scale-input", Input).value = "647.7"
        app.query_one("#fret-count-input", Input).value = "2"
        await pilot.click("#calculate-frets")
        app.query_one("#export-path", Input).value = str(destination)
        await pilot.click("#export-button")

    assert destination.read_text().startswith(
        "fret_number,distance_from_nut_mm,previous_spacing_mm,residual_length_mm\n"
    )


@pytest.mark.asyncio
async def test_text_export_uses_the_selected_format(tmp_path: Path) -> None:
    app = GuitarMakerApp()
    destination = tmp_path / "frets.txt"

    async with app.run_test() as pilot:
        app.query_one("#scale-input", Input).value = "647.7"
        app.query_one("#fret-count-input", Input).value = "2"
        await pilot.click("#calculate-frets")
        app.query_one("#export-path", Input).value = str(destination)
        app.query_one("#export-format", Select).value = "text"
        await pilot.click("#export-button")

    assert destination.read_text().startswith("Fret | Distance from nut (mm)")
