from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:jonathan@localhost:5432/faniloqr")

with engine.connect() as connection:
    resul