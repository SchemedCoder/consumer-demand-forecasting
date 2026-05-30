from sqlalchemy import create_engine

DB_URL = (
    "postgresql://postgres:"
    "postgres@localhost:5432/"
    "consumer_demand"
)

engine = create_engine(DB_URL)
