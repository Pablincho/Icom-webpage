from base import Base
from sqlalchemy import Column, types
from app import db


class HistorialOp(Base, db.Model):
    __tablename__ = 'historialop'

    IdOp = Column(types.Integer, primary_key=True)
    Fecha = Column(types.DateTime, primary_key=True)
    Afectado = Column(types.String(25), primary_key=True)
    Responsable = Column(types.Integer, primary_key=True)

    def __repr__(self):
        enc_historial = self.Afectado.encode('UTF-8')
        return '<HistorialOp {}>'.format(enc_historial)
