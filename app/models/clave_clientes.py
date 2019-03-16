from base import Base
from sqlalchemy import Column, types
from app import db


class ClavesClientes(Base, db.Model):
    __tablename__ = 'clavecli'

    IdCli = Column(types.Integer, primary_key=True)
    Clave = Column(types.Integer, primary_key=True)

    def __repr__(self):
        return '<ClavesClientes {}>'.format(self.Clave)
