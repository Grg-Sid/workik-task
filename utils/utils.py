from utils.db_manager import ServerAuthDBManager, UserAuthDBManager

db_path = "./data/auth.sqlite3"


def server_authenticated(token: str) -> bool:
    server_auth_db = ServerAuthDBManager(db_path)
    query = """SELECT 1 FROM Server WHERE token=? LIMIT 1"""
    result = server_auth_db.select(query, (token,))
    return bool(result)


def user_authenticated(token: str) -> bool:
    user_auth_db = UserAuthDBManager(db_path)
    query = """SELECT 1 FROM User WHERE token=? LIMIT 1"""
    result = user_auth_db.select(query, (token,))
    return bool(result)
