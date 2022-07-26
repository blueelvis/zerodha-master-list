from dotenv import load_dotenv
import os

load_dotenv()

def get_database_credentials():
    return dict({
        "DATABASE_NAME": os.environ['DATABASE_NAME'],
        "DATABASE_HOST": os.environ['DATABASE_HOST'],
        "DATABASE_USERNAME": os.environ['DATABASE_USERNAME'],
        "DATABASE_PASSWORD": os.environ['DATABASE_PASSWORD']
    })