import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
        }


class Features(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    filename = Column(String(250))
    description = Column(String(250))
    year = Column(String(8))
    director = Column(String(250))
    trailer = Column(String(250))
    movie_id = Column(Integer, ForeignKey('movie.id'))
    movie = relationship(Movie)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'filename': self.filename,
            'description': self.description,
            'id': self.id,
            'year': self.year,
            'director': self.director,
            'trailer': self.trailer
        }


engine = create_engine('sqlite:///app.db')


Base.metadata.create_all(engine)
