import os
from flask import Flask
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)

# created variable called supabase which is a client, substantiated with create_client
supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"), 
    os.environ.get("SUPABASE_KEY")
    )

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