from database.db_connection import get_db

class BaseRepository:
    """
    Base class for all repositories.
    Provides helpers to execute queries.
    """

    def fetch_all(self, sql: str, params=None):
        with get_db() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def fetch_one(self, sql: str, params=None):
        with get_db() as cur:
            cur.execute(sql, params)
            return cur.fetchone()

    def execute(self, sql: str, params=None):
        with get_db() as cur:
            cur.execute(sql, params)
