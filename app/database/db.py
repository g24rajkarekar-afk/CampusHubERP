from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///campushub.db"


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)

            cls._instance.engine = create_engine(
                DATABASE_URL,
                echo=False
            )

            cls._instance.SessionLocal = sessionmaker(
                bind=cls._instance.engine,
                autoflush=False,
                autocommit=False
            )

        return cls._instance


# Create the single shared database instance
db = DatabaseSingleton()

engine = db.engine
SessionLocal = db.SessionLocal

Base = declarative_base()