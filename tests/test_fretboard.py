from decimal import Decimal, ROUND_HALF_UP, localcontext

import pytest

from guitar_maker_tools.calculations.fretboard import (
    calculate_fretboard,
    calculate_scale_from_fret_position,
)


def rounded(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def test_calculates_documented_647_7_mm_positions() -> None:
    measurements = calculate_fretboard("647.7", 22)

    assert len(measurements) == 22
    assert rounded(measurements[0].distance_from_nut_mm) == Decimal("36.35")
    assert rounded(measurements[11].distance_from_nut_mm) == Decimal("323.85")
    assert rounded(measurements[21].distance_from_nut_mm) == Decimal("465.95")
    assert rounded(measurements[11].residual_length_mm) == Decimal("323.85")


def test_calculates_documented_630_mm_seventh_fret() -> None:
    seventh_fret = calculate_fretboard("630", 7)[-1]

    assert rounded(seventh_fret.distance_from_nut_mm) == Decimal("209.53")


def test_derives_scale_from_fret_position() -> None:
    position = calculate_fretboard("647.7", 7)[-1].distance_from_nut_mm

    scale = calculate_scale_from_fret_position(position, 7)

    assert abs(scale - Decimal("647.7")) < Decimal("0.0000000001")


@pytest.mark.parametrize(
    ("scale", "fret_count", "message"),
    [
        ("0", 22, "Scale length must be greater than zero."),
        ("NaN", 22, "Scale length must be a finite number."),
        ("647.7", 0, "Fret number must be a positive whole number."),
        ("647.7", True, "Fret number must be a positive whole number."),
    ],
)
def test_rejects_invalid_fretboard_inputs(
    scale: str, fret_count: int, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        calculate_fretboard(scale, fret_count)


def test_previous_spacing_is_derived_from_common_nut_reference() -> None:
    measurements = calculate_fretboard("647.7", 2)

    with localcontext() as context:
        context.prec = 36
        expected_spacing = (
            measurements[1].distance_from_nut_mm
            - measurements[0].distance_from_nut_mm
        )
        assert measurements[1].previous_spacing_mm == expected_spacing
