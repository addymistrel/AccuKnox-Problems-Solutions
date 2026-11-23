from ...database_helpers import execute_query, execute_many, fetch_all
from ..models.user import User


def create_users_table():
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            age INTEGER,
            city TEXT,
            company TEXT
        )
    """

    execute_query(query)


def insert_users(users: list[User]):
    query = """
        INSERT INTO users (name, email, phone, age, city, company)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(email) DO NOTHING
    """

    data = [
        (
            user.name,
            user.email,
            user.phone,
            user.age,
            user.city,
            user.company
        )
        for user in users
    ]

    return execute_many(query, data)


def get_users(limit=10) -> list[User]:
    query = "SELECT name, email, phone, age, city, company FROM users ORDER BY id LIMIT ?"
    rows = fetch_all(query, (limit,))
    return [User(**row) for row in rows]
