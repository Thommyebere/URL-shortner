import sqlite3

connection = sqlite3.connect('urls.db', check_same_thread=False)
connection.row_factory = sqlite3.Row
curs = connection.cursor()

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS URLS
            (id INTEGER PRIMARY KEY, 
            created_date NOT NULL DEFAULT CURRENT_TIMESTAMP, 
            original_URL TEXT NOT NULL, 
            clicks INTEGER NOT NULL DEFAULT 0);"""

INSERT_URL = """INSERT INTO URLS (original_URL) values(?);"""

SELECT_URL = """SELECT original_url from URLS where id=?;"""

def create_table():
    with connection:
        curs.execute(CREATE_TABLE)


def make_record(original_url):
    with connection:
        curs.execute(INSERT_URL, (original_url,))
        return curs.lastrowid


def get_record(id):
    with connection:
        curs.execute(SELECT_URL, (id,))
        return curs.fetchone()


