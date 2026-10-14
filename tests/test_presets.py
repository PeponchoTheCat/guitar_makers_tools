from decimal import Decimal

import pytest

from guitar_maker_tools.presets import SCALE_PRESETS


@pytest.mark.parametrize(
    ("name", "scale_mm"),
    [
        ("Martin standard (25.4 in)", Decimal("645.16")),
        ("Martin short scale (24.9 in)", Decimal("632.46")),
        ("Taylor standard (25.5 in)", Decimal("647.7")),
        ("Taylor GS Mini (23.5 in)", Decimal("596.9")),
    ],
)
def test_brand_scale_presets_are_available(name: str, scale_mm: Decimal) -> None:
    presets_by_name = {preset.name: preset.scale_mm for preset in SCALE_PRESETS}

    assert presets_by_name[name] == scale_mm
