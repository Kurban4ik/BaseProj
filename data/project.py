from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, orm
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

class Project(SqlAlchemyBase):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = orm.relationship("User", backref="projects")
    description = Column(Text)
    completion_date = Column(DateTime)
    status = Column(String)