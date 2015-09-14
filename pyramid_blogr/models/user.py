import datetime #<- will be used to set default dates on models
from pyramid_blogr.models.meta import Base  #<- we need to import our sqlalchemy metadata for model classes to inherit from
from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide unicode field,
    DateTime     #<- time abstraction field,
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    def verify_password(self, password):
        return self.password == password
