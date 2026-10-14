"""Common nominal guitar scale presets."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ScalePreset:
    """A named nominal scale length expressed in millimetres."""

    name: str
    scale_mm: Decimal


SCALE_PRESETS = (
    ScalePreset("Fender (25.5 in)", Decimal("647.7")),
    ScalePreset("Gibson (24.75 in)", Decimal("628.65")),
    ScalePreset("Martin standard (25.4 in)", Decimal("645.16")),
    ScalePreset("Martin short scale (24.9 in)", Decimal("632.46")),
    ScalePreset("Taylor standard (25.5 in)", Decimal("647.7")),
    ScalePreset("Taylor GS Mini (23.5 in)", Decimal("596.9")),
    ScalePreset("Classical (650 mm)", Decimal("650")),
    ScalePreset("Short scale (24 in)", Decimal("609.6")),
)
