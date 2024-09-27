from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, orm
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = orm.relationship("User", backref="tasks")
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = orm.relationship("Project", backref="tasks")
    deadline = Column(DateTime)