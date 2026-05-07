from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)
DATABASE_URL = os.getenv("DATABASE_URL")