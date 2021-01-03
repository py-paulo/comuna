from sanic import Sanic
from sanic_jwt import initialize

from .auth import authenticate, retrieve_user
from .views import status, get_user, create_user, create_article

app = Sanic("Comuna")

app.add_route(status, '/', methods=['GET', 'POST'])
app.add_route(get_user, r'/user/<user_id:\d+>', methods=['GET', 'POST'])
app.add_route(create_user, '/user', methods=['POST'])
app.add_route(create_article, '/article', methods=['POST'])

initialize(app, authenticate=authenticate, retrieve_user=retrieve_user)