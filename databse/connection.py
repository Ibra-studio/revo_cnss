import sqlite3

_connection=None

def get_connection():
    global _connection
    if _connection is None:
        _connection=sqlite3.connect("revo_cnss.db")
        _connection.row_factory=sqlite3.Row
    return _connection

def close_connection():
    global _connection
    if _connection is not None:
        _connection.close()
        _connection=None
    