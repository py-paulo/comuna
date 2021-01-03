from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from sanic_jwt import initialize

from .auth import User, authenticate, retrieve_user

app = Sanic("Comuna")


@app.route("/")
async def test(request):
    return json({"status": "up"})


users = [User(1, "user1", "abcxyz"), User(2, "user2", "abcxyz")]

username_table = {u.username: u for u in users}
userid_table = {u.user_id: u for u in users}

initialize(app, authenticate=authenticate, retrieve_user=retrieve_user)

