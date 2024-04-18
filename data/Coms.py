import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Coms(SqlAlchemyBase):
    __tablename__ = 'komm'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    Name = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    Comm = sqlalchemy.Column(sqlalchemy.String)
    Mark = sqlalchemy.Column(sqlalchemy.Integer)


