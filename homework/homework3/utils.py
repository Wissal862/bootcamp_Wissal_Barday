
import os
from dotenv import load_dotenv

def load_env():
        load_dotenv()

def get_key(key: str):
        return os.getenv(key)
