import os
from utils.db_manager import ServerAuthDBManager, UserAuthDBManager

db_path = os.environ.get("DB_PATH", "./data/auth.sqlite3")


def server_authenticated(token: str) -> bool:
    server_auth_db = ServerAuthDBManager(db_path)
    return server_auth_db.is_present(token)


def user_authenticated(token: str) -> bool:
    user_auth_db = UserAuthDBManager(db_path)
    return user_auth_db.is_present(token)
