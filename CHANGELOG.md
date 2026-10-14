# Changelog

All notable changes to this project are documented in this file.

The project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-14

### Added

- Textual terminal interface for equal-temperament fretboard calculations.
- Forward calculation of fret position, previous spacing, and residual string
  length from a nominal scale.
- Inverse calculation of nominal scale from a fret position.
- Presets for common Fender, Gibson, Martin, Taylor, classical, and short-scale
  instruments.
- CSV and fixed-width text exports with three-decimal measurements.
- Visual reference highlights for the 12th and 14th fret rows.
- Explicit Quit button and `Q` keyboard shortcut.
- Project, usage, and calculation-theory documentation.

### Fixed

- Corrected documented fret-position examples to match the stated
  equal-temperament formula.
- Kept calculation, export, and quitting controls visible in a standard
  terminal viewport.
