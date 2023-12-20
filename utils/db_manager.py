import mysql.connector
from abc import ABC, abstractmethod


class DBManager(ABC):
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "root"
        database = "auth"
        self.connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.connection.cursor()

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def is_present(self):
        pass

    @abstractmethod
    def truncate(self):
        pass


class ServerAuthDBManager(DBManager):
    def create_table(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS Server (ID INT AUTO_INCREMENT PRIMARY KEY, token VARCHAR(255) UNIQUE)"""
            self.cursor.execute(query)
            self.connection.commit()
            print("Table created successfully")
        except mysql.connector.Error as e:
            print(e)

    def insert(self, token):
        try:
            query = """INSERT INTO Server (token) VALUES (%s)"""
            self.cursor.execute(query, (token,))
            self.connection.commit()
            print("Data inserted successfully")
            return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def is_present(self, token):
        try:
            query = """SELECT 1 FROM Server WHERE token=%s LIMIT 1"""
            self.cursor.execute(query, (token,))
            result = self.cursor.fetchone()

            if result:
                print("Data is present in Server DB")
                return True
            else:
                print("Data is not present in Server DB")
                return False

        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")
            return False

    def truncate(self):
        try:
            query = """DELETE FROM Server"""
            self.cursor.execute(query)
            self.connection.commit()
            print("Data truncated successfully")
        except mysql.connector.Error as e:
            print(e)


class UserAuthDBManager(DBManager):
    def create_table(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS User (ID INT AUTO_INCREMENT PRIMARY KEY, token VARCHAR(255) UNIQUE)"""
            self.cursor.execute(query)
            self.connection.commit()
            print("Table created successfully")
        except mysql.connector.Error as e:
            print(e)

    def insert(self, token):
        try:
            query = """INSERT INTO User (token) VALUES (%s)"""
            self.cursor.execute(query, (token,))
            self.connection.commit()
            print("Data inserted successfully")
            return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def is_present(self, token):
        try:
            query = """SELECT 1 FROM User WHERE token=%s LIMIT 1"""
            self.cursor.execute(query, (token,))
            result = self.cursor.fetchone()

            if result:
                print("Data is present in User DB")
                return True
            else:
                print("Data is not present in User DB")
                return False

        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")
            return False

    def truncate(self):
        try:
            query = """DELETE FROM User"""
            self.cursor.execute(query)
            self.connection.commit()
            print("Data truncated successfully")
        except mysql.connector.Error as e:
            print(e)
