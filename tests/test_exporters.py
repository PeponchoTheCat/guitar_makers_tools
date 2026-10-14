from pathlib import Path

from guitar_maker_tools.calculations.fretboard import calculate_fretboard
from guitar_maker_tools.exporters import (
    fretboard_to_csv,
    fretboard_to_text,
    write_export,
)


def test_csv_contains_headers_and_three_decimal_values() -> None:
    content = fretboard_to_csv(calculate_fretboard("647.7", 1))

    lines = content.splitlines()
    assert lines[0] == (
        "fret_number,distance_from_nut_mm,previous_spacing_mm,residual_length_mm"
    )
    assert lines[1] == "1,36.353,36.353,611.347"


def test_text_export_is_human_readable() -> None:
    content = fretboard_to_text(calculate_fretboard("647.7", 1))

    assert "Distance from nut (mm)" in content
    assert "36.353" in content


def test_text_export_handles_an_empty_table() -> None:
    assert fretboard_to_text(()) == (
        "Fret | Distance from nut (mm) | Previous spacing (mm) | Residual length (mm)\n"
    )


def test_write_export_creates_requested_file(tmp_path: Path) -> None:
    destination = tmp_path / "fretboard.csv"

    result = write_export(destination, "example\n")

    assert result == destination
    assert destination.read_text() == "example\n"
