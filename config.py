import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Alzheimer's Preventor API"
    VERSION = "1.0.0"
    # Use SQLite for now. It will create a file called 'app.db' in your project.
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")

settings = Settings()
