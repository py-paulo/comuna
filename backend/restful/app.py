from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_jwt import initialize

from .auth import User, authenticate, retrieve_user

app = Sanic("Comuna")


async def status(request):
    return json({"status": "up"})

async def get_user(request):
    return json({})

async def create_user(request):
    return json({})

async def create_article(request):
    return json({})


app.add_route(status, '/', methods=['GET', 'POST'])
app.add_route(get_user, r'/user/<id:[\d+]>', methods=['GET', 'POST'])
app.add_route(create_user, '/user', methods=['POST'])
app.add_route(create_article, '/article', methods=['POST'])


initialize(app, authenticate=authenticate, retrieve_user=retrieve_user)