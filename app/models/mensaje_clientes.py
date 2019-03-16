from base import Base
from sqlalchemy import Column, types
from app import db


class MensajeClientes(Base, db.Model):
    __tablename__ = 'mensajecli'

    Clave = Column(types.Integer, primary_key=True)
    Fecha = Column(types.Date, primary_key=True)
    Hora = Column(types.String(10), primary_key=True)
    Contenido = Column(types.String(255), primary_key=True)

    def __repr__(self):
        return '<MensajeClientes {}>'.format(self.Clave)
