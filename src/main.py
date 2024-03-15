from random import randint
from typing import Union, List
import hashlib
from fastapi import FastAPI
from schemas import CreateUser, ReadUser

app = FastAPI(title="Трекер задач", description="API для приложения "
                                                "отлеживания задач")

users = {}


class User:
    def __init__(self, first_name, last_name, username, password, bdate,
                 bio, email):
        self.first_name = first_name # STR
        self.last_name = last_name # STR
        self.username = username # STR
        self.password = password # STR
        self.bdate = bdate # datetime
        self.bio = bio # STR
        self.email = email # STR

    @property
    def hash_password(self):
        return ''.join([i+str(randint(1, 100)) for i in self.password])

    def out(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'password': self.hash_password,
            'bdate': self.bdate,
            'bio': self.bio,
            'email': self.email

        }

@app.get('/')
async def hello():
    return {"Hello": "World"}


@app.get('/hello/{user}')
async def hello_sb(user):
    return {"Hello": user}


@app.get('/when/{year}')
async def when(year:int) -> dict:
    if int(year) < 2024:
        return {"Year": 2024-int(year)}
    return {
        'error': "надо меньше 2024"
    }


@app.post('/user')
async def add_user(user: CreateUser) -> ReadUser:
    if not users.keys():
        new_id = '1'
    else:
        new_id = str(max([int(i) for i in users.keys()])+1)
    users[new_id] = User(user.first_name, user.last_name, user.username, user.password, user.bdate, user.bio, user.email)
    return users[new_id].out()


@app.get('/user')
async def get_users():
    return {i: users[i].out() for i in users.keys()}

