from base import Base
from sqlalchemy import Column, types
from app import db


class Operaciones(Base, db.Model):
    __tablename__ = 'operaciones'

    IdOp = Column(types.Integer, primary_key=True)
    Operacion = Column(types.String(25))

    def __repr__(self):
        return '<Operaciones {}>'.format(self.Operacion)
