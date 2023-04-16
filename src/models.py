import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    personajes_favoritos = relationship('FavoritoPersonaje', back_populates='usuario')
    hechizos_favoritos = relationship('FavoritoHechizo', back_populates='usuario')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(500))
    imagen = Column(String(1000))
    favoritos = relationship('FavoritoPersonaje', back_populates='personaje')

class Hechizo(Base):
    __tablename__ = 'hechizo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(500))
    imagen = Column(String(1000))
    favoritos = relationship('FavoritoHechizo', back_populates='hechizo')

class FavoritoPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    usuario = relationship('Usuario', back_populates='personajes_favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

class FavoritoHechizo(Base):
    __tablename__ = 'favorito_hechizo'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_hechizo = Column(Integer, ForeignKey('hechizo.id'))
    usuario = relationship('Usuario', back_populates='hechizos_favoritos')
    hechizo = relationship('Hechizo', back_populates='favoritos')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
