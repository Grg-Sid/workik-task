import sqlite3
from abc import ABC, abstractmethod


class DBManager(ABC):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def truncate(self):
        pass


class ServerAuthDBManager(DBManager):
    def create_table(self) -> sqlite3.Connection:
        try:
            query = """CREATE TABLE IF NOT EXISTS Server (ID INTEGER PRIMARY KEY, token TEXT UNIQUE)"""
            self.cursor.execute(query)
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(e)

        return self.conn

    def insert(self, token: str) -> bool:
        try:
            query = """INSERT INTO Server (token) VALUES (?)"""
            self.cursor.execute(query, (token,))
            self.conn.commit()
            print("Data inserted successfully")
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def truncate(self):
        try:
            query = """DELETE FROM Server"""
            self.cursor.execute(query)
            self.conn.commit()
            print("Data truncated successfully")
        except sqlite3.Error as e:
            print(e)


class UserAuthDBManager(DBManager):
    def create_table(self) -> sqlite3.Connection:
        try:
            query = """CREATE TABLE IF NOT EXISTS User (ID INTEGER PRIMARY KEY, token TEXT UNIQUE)"""
            self.cursor.execute(query)
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(e)

        return self.conn

    def insert(self, token: str) -> bool:
        try:
            query = """INSERT INTO User (token) VALUES (?)"""
            self.cursor.execute(query, (token,))
            self.conn.commit()
            print("Data inserted successfully")
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def truncate(self):
        try:
            query = """DELETE FROM User"""
            self.cursor.execute(query)
            self.conn.commit()
            print("Data truncated successfully")
        except sqlite3.Error as e:
            print(e)
