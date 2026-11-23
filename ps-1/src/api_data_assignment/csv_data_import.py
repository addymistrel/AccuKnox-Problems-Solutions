import csv

from ..config import DATA_DIR
from .models.user import User
from .repository.users_repo import create_users_table, get_users, insert_users


CSV_PATH = DATA_DIR / "users_with_details.csv"


def import_users(csv_path=CSV_PATH):
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    users = [
        User(
            name=row["name"].strip(),
            email=row["email"].strip(),
            phone=row["phone"].strip(),
            age=int(row["age"]),
            city=row["city"].strip(),
            company=row["company"].strip()
        )
        for row in rows
    ]

    return insert_users(users)


def print_users(users: list[User]):
    if not users:
        print("No users found.")
        return

    for index, user in enumerate(users, start=1):
        print(f"\n--------- User {index} ----------")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone or 'N/A'}")
        print(f"Age: {user.age or 'Unknown'}")
        print(f"City: {user.city or 'N/A'}")
        print(f"Company: {user.company or 'N/A'}")
        print("-" * 35)


def process_csv_import():
    create_users_table()
    inserted_count = import_users()
    users = get_users(limit=10)
    return inserted_count, users