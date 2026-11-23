import sqlite3
from pathlib import Path

from .config import DB_PATH


def get_connection():
    Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def execute_query(query, params=()):
    conn = get_connection()

    try:
        cursor = conn.execute(query, params)
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()


def execute_many(query, data):
    conn = get_connection()

    try:
        cursor = conn.executemany(query, data)
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()


def fetch_all(query, params=()):
    conn = get_connection()

    try:
        cursor = conn.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def fetch_one(query, params=()):
    conn = get_connection()

    try:
        cursor = conn.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()