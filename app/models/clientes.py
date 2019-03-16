from base import Base
from sqlalchemy import Column, types
from app import db


class Clientes(Base, db.Model):
    __tablename__ = 'clientes'

    idCli = Column(types.Integer, primary_key=True)
    NombreCli = Column(types.String(20))
    Password = Column(types.String(12))
    IdGrupo = Column(types.Integer)

    def __repr__(self):
        enc_nombre = self.NombreCli.encode('UTF-8')
        return '<Clientes {}>'.format(enc_nombre)
