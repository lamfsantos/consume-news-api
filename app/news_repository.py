import sqlite3
from sqlite3 import Error
import datetime
import json

database = r"pythonsqlite.db"

def create_connection():
    conn =None
    try:
        conn = sqlite3.connect(database)
    except Exception as e:
        print(e)

    return conn

def find_by_country(country):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT news_json, last_update FROM news WHERE country = ?", (country, ))
    rows = c.fetchall()
    return rows

def insert(news_json, country):
    currentDT = datetime.datetime.now()
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO news VALUES (?, ?, ?)", (json.dumps(news_json), country, currentDT))
    conn.commit()
    conn.close()

def delete_by_time(last_update):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM news WHERE last_update = ?", (last_update, ))
    conn.commit()
    conn.close()
