from typing import List
from sqlalchemy.orm.session import Session
from sqlalchemy import func


class MSSQLSession:
    """
        Connection credentials comes to class as **kwargs.
        Fetchall method should be used to small datasets
    """

    def __init__(self, session: Session):
        self.session = session

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fetch_all(self, query, params=None):
        cursor = self.session.execute(query, params).cursor
        return cursor.fetchall()

    def fetch_one(self, query):
        cursor = self.session.execute(query).cursor
        return cursor.fetchone()

    def copy_from(self, file, table_name, **kwargs):
        cursor = self.session.connection().connection.cursor()
        cursor.copy_from(file, table_name, **kwargs)

    def execute(self, query, params=None):
        self.session.execute(query, params)
        self.commit()

    def fetch(self, query):
        cursor = self.session.execute(query).cursor
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row

    def call_proc(self, function_name: str, parameters: list):
        cursor = self.session.connection().connection.cursor()
        cursor.callproc(function_name, parameters)
        self.commit()
        return cursor.fetchall()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()
