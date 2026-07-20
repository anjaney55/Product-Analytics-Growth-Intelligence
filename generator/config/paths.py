from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

CLEANED_DATA_DIR = DATA_DIR / "cleaned"

WAREHOUSE_DATA_DIR = DATA_DIR / "warehouse"

LOG_DIR = ROOT_DIR / "logs"
