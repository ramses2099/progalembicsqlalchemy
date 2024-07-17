from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(url="postgresql://postgres:S3cret@10.0.0.50/alembic_db")
session = scoped_session(sessionmaker(autoflush=False,
                                      autocommit=False, bind=engine))
