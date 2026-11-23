from ...database_helpers import execute_query, execute_many, fetch_all
from ..models.book import Book


def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER,
            documentation_url TEXT
        )
    """

    execute_query(query)


def insert_books(books: list[Book]):
    query = """
        INSERT INTO books (
            book_id,
            title,
            author,
            publication_year,
            documentation_url
        )
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(book_id) DO NOTHING
    """

    data = [
        (
            book.book_id,
            book.title,
            book.author,
            book.publication_year,
            book.documentation_url
        )
        for book in books
    ]

    return execute_many(query, data)


def get_all_books(name_search: str = "", limit: int = 10) -> list[Book]:
    query = "SELECT * FROM books "
    params = []

    if name_search:
        query += "WHERE title LIKE ? "
        params.append(f"%{name_search}%")

    query += "ORDER BY id LIMIT ?"
    params.append(limit)

    rows = fetch_all(query, tuple(params))

    return [Book(**row) for row in rows]