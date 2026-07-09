"""
Greyhound Engine
Version 0.2.0

Main entry point.
"""

from engine.data_loader import DataLoader


def main():
    print("=" * 60)
    print("           GREYHOUND ENGINE")
    print("              Version 0.2.0")
    print("=" * 60)

    loader = DataLoader()

    print("\nChecking data folder...")
    loader.list_files()

    print("\nSystem ready.")


if __name__ == "__main__":
    main()
    