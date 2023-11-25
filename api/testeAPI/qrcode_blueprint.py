import os
from dotenv import load_dotenv
from supabase import create_client, Client
from flask import Blueprint, jsonify

qrcode = Blueprint('qrcode', __name__)

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

@qrcode.route("/business", methods=['GET'])
def exibir_business():
    
    response = supabase.table('Business').select("*").execute()

    return jsonify(response.data)

