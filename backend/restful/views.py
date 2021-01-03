import peewee

from sanic_jwt import protected
from sanic.log import logger
from sanic.response import json

from .models import User

async def status(request):
    return json({"status": "up"})

@protected()
async def get_user(request, user_id):
    user = None
    try:
        user = User.select().where(User.id == user_id).get()
    except peewee.DoesNotExist:
        return json({})
    return json(user.to_dict)

@protected()
async def create_user(request):
    return json({})

@protected()
async def create_article(request):
    return json({})