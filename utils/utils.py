import os
from utils.db_manager import ServerAuthDBManager, UserAuthDBManager


def server_authenticated(token: str) -> bool:
    server_auth_db = ServerAuthDBManager()
    return server_auth_db.is_present(token)


def user_authenticated(token: str) -> bool:
    user_auth_db = UserAuthDBManager()
    return user_auth_db.is_present(token)
