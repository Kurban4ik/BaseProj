from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, orm
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class relations(SqlAlchemyBase):
    __tablename__ = 'relations'
    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('users.id'))
    worker_id = Column(Integer, ForeignKey('users.id'))
    project = orm.relationship("Users", backref="relation")