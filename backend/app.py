from sanic import Sanic
from sanic.response import json

app = Sanic("Comuna")


@app.route("/")
async def test(request):
    return json({"status": "up"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, access_log=True)
