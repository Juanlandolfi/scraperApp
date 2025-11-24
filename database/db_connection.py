import os
import psycopg2
from dotenv import load_dotenv
from contextlib import contextmanager
from psycopg2.extensions import cursor as PsycopgCursor
from typing import Iterator




load_dotenv()

DB_USER = os.getenv("DB_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")



# Returns cursor. Commit and close.
@contextmanager
def get_db() -> Iterator[PsycopgCursor]:
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DATABASE
        )
        
        cursor = connection.cursor()
        yield cursor
        connection.commit()
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
