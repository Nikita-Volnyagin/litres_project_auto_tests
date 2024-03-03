from dotenv import load_dotenv
import os

load_dotenv()
base_url = "https://api.litres.ru/foundation/api"
url = "/auth/login"
user_email = os.getenv('USER_EMAIL')
user_password = os.getenv('USER_PASSWORD')
invalid_password = os.getenv('UNREGISTERED_USER_PASSWORD')
headers = {"Content-Type": "application/json"}
