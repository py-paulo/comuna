import sys

from .settings import config
from .errors import errors

from .app import app

if __name__ == "__main__":
    sanic_config = config.get('sanic', {})

    if not config:
        sys.exit(errors.CONFIGURATION_FILE_NOT_FOUND)

    app.run(host=sanic_config.get('host'), port=sanic_config.get('port'),
        debug=sanic_config.get('debug'), access_log=sanic_config.get('access_log'))