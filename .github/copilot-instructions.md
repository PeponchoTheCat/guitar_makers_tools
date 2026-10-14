# Copilot instructions

## Commands

This development machine uses Conda. Activate the existing `guitar_tools`
environment before running project commands:

```bash
conda activate guitar_tools
```

Install the project and development dependencies inside that environment:

```bash
python -m pip install -e ".[dev]"
```

Run the full test suite:

```bash
pytest
```

Run one test:

```bash
pytest tests/test_fretboard.py::test_calculates_documented_647_7_mm_positions
```

No linter or formatter command is configured in `pyproject.toml`.

Launch the terminal application after installation:

```bash
guitar-maker-tools
```

## Architecture

- `app/guitar_maker_tools/calculations/fretboard.py` is the pure
  equal-temperament domain layer. It validates scale and fret inputs and
  returns immutable `FretMeasurement` records.
- `app/guitar_maker_tools/ui/app.py` owns the Textual widgets and translates
  user actions into domain calls. Keep mathematical or export logic out of
  this layer.
- `app/guitar_maker_tools/exporters.py` serializes a calculated table to CSV
  or fixed-width text and atomically writes exports.
- `app/guitar_maker_tools/presets.py` is the single source of named nominal
  scale lengths.
- `tests/test_fretboard.py` covers the documented mathematical examples,
  `tests/test_exporters.py` covers serialization and writing, and
  `tests/test_ui.py` exercises Textual interactions with `run_test`.

## Project conventions

- Measurements are in millimetres. A fret position is always measured from the
  nut edge facing the bridge; bridge intonation compensation is not part of
  the calculations.
- Retain `Decimal` values through domain and export code. Use
  `format_millimetres` only at display boundaries: UI and all export formats
  show three decimal places.
- Calculate every fret position from the common nut reference, not by
  accumulating rounded inter-fret distances. Preserve the 36-digit local
  calculation precision and validate the documented 12th-fret midpoint and
  scale examples when altering formulas.
- Surface invalid input and export failures through explicit `ValueError` or
  `OSError` handling. Exports are written through a temporary sibling file and
  `os.replace`; preserve this atomic-write behavior.
- Textual widget IDs (`#scale-input`, `#fret-count-input`, `#results`, and
  related controls) form the UI-test contract. Update the tests when changing
  their behavior or identifiers.
