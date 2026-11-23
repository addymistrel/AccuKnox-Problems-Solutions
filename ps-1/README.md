# PS-1: API, Data, and Database Solutions

This project contains solutions for:

1. Fetching and storing books from an external API in SQLite.
2. Fetching student scores from a CSV URL, calculating averages, and creating a bar chart.
3. Importing user information from a local CSV file into SQLite.

## Requirements

- Python 3.11 or later
- Internet connection
- A virtual environment

Required Python packages:

- requests
- pandas
- matplotlib
- pydantic

## Setup

Open a terminal in the `ps-1` directory:

```powershell
cd D:\My_Files\Projects\AccuKnox-Problems-Solutions\ps-1
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install requests pandas matplotlib pydantic
```

## Run the Main Script

Run all three solutions from the project directory:

```powershell
python main.py
```

The program will:

- Fetch Python books and store them in SQLite.
- Download student scores and save a bar chart.
- Import users from the local CSV file into SQLite.

## External APIs

### Open Library Search API

URL:

```text
https://openlibrary.org/search.json?q=python
```

The application sends an HTTP GET request to the Open Library Search API and retrieves books related to Python.

Example parameters used:

```text
q=python
limit=100
fields=key,title,author_name,first_publish_year
```

Retrieved data includes:

- Book key
- Title
- Author names
- First publication year

The book records are stored in the `books` table.

### GitHub Raw Student Scores CSV

URL:

```text
https://raw.githubusercontent.com/ciDSproj/students_scores/refs/heads/main/Students%20Scores.csv
```

The application uses `pandas.read_csv()` to download the CSV directly from GitHub.

Important columns:

- `MathScore`
- `ReadingScore`
- `WritingScore`

The application calculates the average for every subject and creates:

```text
ps-1/outputs/average_student_scores.png
```

## Local CSV Import

The local user CSV is located at:

```text
ps-1/data/users_with_details.csv
```

Its columns are:

- `name`
- `email`
- `phone`
- `age`
- `city`
- `company`

The records are stored in the `users` table.

## SQLite Database

The SQLite database is created at:

```text
ps-1/database/assignment.db
```

It contains:

- `books`
- `users`

## Project Structure

```text
ps-1/
├── main.py
├── README.md
├── data/
│   └── users_with_details.csv
├── database/
│   └── assignment.db
├── outputs/
│   └── average_student_scores.png
└── src/
    ├── config.py
    ├── database_helpers.py
    └── api_data_assignment/
        ├── api_data_retrieval_and_storage.py
        ├── data_process_and_visualization.py
        ├── csv_data_import.py
        ├── models/
        │   ├── book.py
        │   └── user.py
        └── repository/
            ├── books_repo.py
            └── users_repo.py
```
