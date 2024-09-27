from . import users
from . import project
from sqlalchemy.orm import sessionmaker
from db_session import create_session

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

projects = session.query(Project).all() #Можно ли тогда из сессии вытащить ещё и пользователя?

for project in projects:
    print(f"Project ID: {project.id}, Name: {project.name}, Admin ID: {project.admin_id}, Description: {project.description}, completion_date: {completion_date}, status: {status}")

#user_id = currentuser #Короче, тот юзер, который нас интересует


# Если ответ на предыдущий вопрос да, то тупо по аналогии дописываем код, но заниматься таким ночью желания нет

