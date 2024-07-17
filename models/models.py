from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.orm import declarative_base, Relationship
from models.connection import session

Base = declarative_base()
metadata = Base.metadata
Base.query = session.query_property()


class TimeStampeModel(Base):
    __abstract__ = True
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

class User(TimeStampeModel):
    __tablename__="users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(320), nullable=False, unique=True)
    
    preference = Relationship("Preference", back_populates="user", uselist=False, passive_deletes=True)
    addresses = Relationship("Address", back_populates="user", passive_deletes=True)
    
    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.first_name} {self.last_name}"    
    
class Preference(TimeStampeModel):
    __tablename__ ="preferences"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(80), nullable=False)
    currency = Column(String(80), nullable=False)
    # one to one relationship
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True, unique=True)
    
    user = Relationship("User", back_populates="preference")
    
class Address(TimeStampeModel):
    __tablename__ ="address"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    road_name = Column(String(80), nullable=False)
    postcode = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    # one to many relationship
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    user = Relationship("User", back_populates="addresses")
    
    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.city}"    
    
class Role(TimeStampeModel):
    __tablename__ ="roles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    slug = Column(String(80), nullable=False, unique=True)
    
    def __repr__(self):
        return f"{self.__class__.__name__}, name:{self.name}"