"""
Greyhound Engine
Data Loader
"""

from pathlib import Path


class DataLoader:
    def __init__(self):
        self.data_folder = Path("data")

    def list_files(self):
        print(f"Looking inside: {self.data_folder.resolve()}")

        if not self.data_folder.exists():
            print("❌ Data folder not found.")
            return

        files = list(self.data_folder.iterdir())

        if not files:
            print("⚠️ No datasets found.")
            return

        print("\nDatasets detected:\n")

        for file in files:
            print(f"✓ {file.name}")
            