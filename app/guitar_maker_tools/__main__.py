"""CLI entry point for Guitar Maker Tools."""

from .ui.app import GuitarMakerApp


def main() -> None:
    """Run the Textual application."""
    GuitarMakerApp().run()


if __name__ == "__main__":
    main()
