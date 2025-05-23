from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///hospital.db"

engine = create_engine(DATABASE_URL, echo=True)
Sessionlocal = sessionmaker(bind=engine)
Base  = declarative_base()