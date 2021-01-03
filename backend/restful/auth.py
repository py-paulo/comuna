import peewee

from sanic_jwt import exceptions

from .models import User


async def authenticate(request, *args, **kwargs):
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        raise exceptions.AuthenticationFailed('Missing username or password.')

    user = None
    try:
        user = User.select().where(User.username == username).get()
    except peewee.DoesNotExist:
        pass

    if user is None:
        raise exceptions.AuthenticationFailed('User not found.')

    if password != user.password:
        raise exceptions.AuthenticationFailed('Password is incorrect.')

    return user


async def retrieve_user(request, payload, *args, **kwargs):
    if not payload:
        return None

    user_id = payload.get('user_id', None)
    try:
        user = User.select().where(User.id == user_id).get()
    except peewee.DoesNotExist:
        user = None

    return user