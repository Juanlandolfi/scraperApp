from db_connection import get_db


class DB:
    def query(self, sql: str, params=None):
        with get_db() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def execute(self, sql: str, params=None):
        with get_db() as cur:
            cur.execute(sql, params)