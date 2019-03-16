from base import Base
from sqlalchemy import Column, types
from app import db


class Grupos(Base, db.Model):
    __tablename__ = 'grupos'

    idGrupo = Column(types.Integer, primary_key=True)
    Grupo = Column(types.String(15))
    IsActive = Column(types.Boolean)

    def __repr__(self):
        enc_grupo = self.Grupo.encode('UTF-8')
        return '<Grupos {}>'.format(enc_grupo)
