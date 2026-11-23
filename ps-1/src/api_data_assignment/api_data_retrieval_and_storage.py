import requests

from ..config import BOOKS_API_URL
from .models.book import Book
from .repository.books_repo import insert_books, create_table, get_all_books


class Books:
    def __init__(self):
        create_table()
        print("Fetching and storing Books into DB...")
        self._fetch_and_store_books()

    def _fetch_and_store_books(self) -> None:
        response = requests.get(
            BOOKS_API_URL,
            params={
                "q": "python",
                "limit": 100,
                "fields": "key,title,author_name,first_publish_year"
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        books = []

        for item in data.get("docs", []):
            if not item.get("key") or not item.get("title"):
                continue

            book = Book(
                book_id=item["key"],
                title=item["title"],
                author=", ".join(item.get("author_name", [])) or None,
                publication_year=item.get("first_publish_year"),
                documentation_url=f"https://openlibrary.org{item['key']}"
            )

            books.append(book)

        insert_books(books)

    def get_all_books(self, nameSearch='', limit=10) -> list[Book]:
        books = get_all_books(nameSearch, limit)
        return books

    def print_books(self, books: list[Book]) -> None:
        if not books:
            print("No books found.")
            return

        for index, book in enumerate(books, start=1):
            print(f"\n--------- Book {index} ----------")
            print(f"Book ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author or 'Unknown'}")
            print(f"Publication Year: {book.publication_year or 'Unknown'}")
            print(f"Documentation URL: {book.documentation_url or 'N/A'}")
            print("-" * 35)
            print()