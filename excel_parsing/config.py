from pathlib import Path

import psycopg2

path = Path(__name__).resolve().parent
SPREADSHEET_PATH = path / 'excel_parsing/testing.xlsx'


def get_pg_connection():
    conn = psycopg2.connect(host='94.103.88.5',
                            port='32769',
                            database='urcop',
                            user='urcop',
                            password='urcop')
    conn.autocommit = True
    return conn
