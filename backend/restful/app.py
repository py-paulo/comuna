from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_jwt import initialize

from .auth import User, authenticate, retrieve_user

app = Sanic("Comuna")


@app.route("/")
async def test(request):
    return json({"status": "up"})

initialize(app, authenticate=authenticate, retrieve_user=retrieve_user)

