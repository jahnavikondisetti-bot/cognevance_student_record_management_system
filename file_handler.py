
import json
from pathlib import Path

# Get the project directory
BASE_DIR = Path(__file__).resolve().parent

# JSON data file location
DATA_FILE = BASE_DIR / "data" / "students.json"


def load_students():
    """Load student records from JSON file."""

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)

            if not isinstance(students, list):
                print("Error: Invalid student data format!")
                return []

            return students

    except json.JSONDecodeError:
        print("Error: Student data file is corrupted!")
        return []

    except OSError as error:
        print("File reading error:", error)
        return []


def save_students(students):
    """Save student records to JSON file."""

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError as error:
        print("File saving error:", error)
        return False
