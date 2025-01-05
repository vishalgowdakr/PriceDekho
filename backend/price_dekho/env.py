from pathlib import Path
from dotenv import load_dotenv

def set_env():
    """Load environment variables from .env file"""
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(env_path)
