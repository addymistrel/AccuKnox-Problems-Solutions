from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
DATABASE_DIR = PROJECT_ROOT / "database"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
DATABASE_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATABASE_DIR / "assignment.db"

BOOKS_API_URL = "https://openlibrary.org/search.json"