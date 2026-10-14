"""Equal-temperament fretboard calculations."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, localcontext
from math import isfinite


CALCULATION_PRECISION = 36


@dataclass(frozen=True)
class FretMeasurement:
    """The theoretical dimensions associated with a fret."""

    fret_number: int
    distance_from_nut_mm: Decimal
    previous_spacing_mm: Decimal
    residual_length_mm: Decimal


def _positive_decimal(value: Decimal | str | int | float, field_name: str) -> Decimal:
    """Convert a finite positive input to Decimal."""
    try:
        if isinstance(value, float) and not isfinite(value):
            raise ValueError
        decimal_value = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise ValueError(f"{field_name} must be a finite number.") from error

    if not decimal_value.is_finite():
        raise ValueError(f"{field_name} must be a finite number.")
    if decimal_value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return decimal_value


def _valid_fret_number(fret_number: int) -> int:
    """Validate an integer fret number."""
    if isinstance(fret_number, bool) or not isinstance(fret_number, int):
        raise ValueError("Fret number must be a positive whole number.")
    if fret_number < 1:
        raise ValueError("Fret number must be a positive whole number.")
    return fret_number


def _semitone_ratio(fret_number: int) -> Decimal:
    """Return 2 raised to fret_number divided by 12."""
    with localcontext() as context:
        context.prec = CALCULATION_PRECISION
        return Decimal(2) ** (Decimal(fret_number) / Decimal(12))


def calculate_fretboard(
    scale_mm: Decimal | str | int | float, fret_count: int
) -> tuple[FretMeasurement, ...]:
    """Calculate theoretical equal-temperament dimensions for each fret."""
    scale = _positive_decimal(scale_mm, "Scale length")
    count = _valid_fret_number(fret_count)
    measurements: list[FretMeasurement] = []
    previous_position = Decimal(0)

    with localcontext() as context:
        context.prec = CALCULATION_PRECISION
        for fret_number in range(1, count + 1):
            ratio = _semitone_ratio(fret_number)
            residual_length = scale / ratio
            position = scale - residual_length
            measurements.append(
                FretMeasurement(
                    fret_number=fret_number,
                    distance_from_nut_mm=position,
                    previous_spacing_mm=position - previous_position,
                    residual_length_mm=residual_length,
                )
            )
            previous_position = position

    return tuple(measurements)


def calculate_scale_from_fret_position(
    distance_from_nut_mm: Decimal | str | int | float, fret_number: int
) -> Decimal:
    """Derive a nominal scale from a theoretical fret position."""
    distance = _positive_decimal(distance_from_nut_mm, "Fret position")
    fret = _valid_fret_number(fret_number)

    with localcontext() as context:
        context.prec = CALCULATION_PRECISION
        ratio = _semitone_ratio(fret)
        return distance / (Decimal(1) - (Decimal(1) / ratio))
