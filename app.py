import os
import sqlite3
from flask import Flask
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)

connection = sqlite3.connect("nameofdatabase.db")
cursor = connection.cursor()

# write raw SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_user_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    username TEXT UNIQUE
               )
""")

connection.commit()

@app.get("/")
def root_route():
    return{"status": "alive"}

# grab test user
@app.get("/api/get-user")
def get_user():
    response = supabase.table("test_user_table").select("*").execute()
    return {"user": response}

if __name__ == '__main__':
    app.run(debug=True)