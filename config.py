# --- config.py ---

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'YOUR_SUPER_SECRET_KEY_HERE' 
SITE_PASSWORD = "admin"  

# JSON Data file Configuration

STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
JSON_DATA_FILE_NAME = 'chat_data.json'
UPLOAD_FOLDER_NAME = 'uploads' # static/uploads

