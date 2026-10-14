"""Export calculated fretboard measurements."""

import csv
import os
from decimal import Decimal, ROUND_HALF_UP
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile

from .calculations.fretboard import FretMeasurement


DISPLAY_PRECISION = Decimal("0.001")


def format_millimetres(value: Decimal) -> str:
    """Format a millimetre value for human-readable output."""
    return format(value.quantize(DISPLAY_PRECISION, rounding=ROUND_HALF_UP), "f")


def fretboard_to_csv(measurements: tuple[FretMeasurement, ...]) -> str:
    """Serialize measurements to CSV using three decimal places."""
    output = StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(
        (
            "fret_number",
            "distance_from_nut_mm",
            "previous_spacing_mm",
            "residual_length_mm",
        )
    )
    for measurement in measurements:
        writer.writerow(
            (
                measurement.fret_number,
                format_millimetres(measurement.distance_from_nut_mm),
                format_millimetres(measurement.previous_spacing_mm),
                format_millimetres(measurement.residual_length_mm),
            )
        )
    return output.getvalue()


def fretboard_to_text(measurements: tuple[FretMeasurement, ...]) -> str:
    """Render measurements as a human-readable fixed-width table."""
    headers = ("Fret", "Distance from nut (mm)", "Previous spacing (mm)", "Residual length (mm)")
    rows = [
        (
            str(measurement.fret_number),
            format_millimetres(measurement.distance_from_nut_mm),
            format_millimetres(measurement.previous_spacing_mm),
            format_millimetres(measurement.residual_length_mm),
        )
        for measurement in measurements
    ]
    if not rows:
        return " | ".join(headers) + "\n"
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    header_line = " | ".join(
        header.ljust(widths[index]) for index, header in enumerate(headers)
    )
    separator = "-+-".join("-" * width for width in widths)
    body = [
        " | ".join(value.rjust(widths[index]) for index, value in enumerate(row))
        for row in rows
    ]
    return "\n".join((header_line, separator, *body, ""))


def write_export(path: str | Path, content: str) -> Path:
    """Atomically write an export, raising an OSError if it cannot be created."""
    destination = Path(path).expanduser()
    if not destination.name:
        raise ValueError("Export path must include a file name.")

    temporary_path: Path | None = None
    try:
        with NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_file.write(content)
            temporary_path = Path(temporary_file.name)
        os.replace(temporary_path, destination)
    except OSError:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise
    return destination
