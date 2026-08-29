from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.models import Base

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"mysql+pymysql://root:{quote_plus(DB_PASSWORD)}"
    f"@127.0.0.1:3306/cloud_migration_advisor"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)