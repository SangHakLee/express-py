from ..app import app

def createServer():
    app.run(
        host="0.0.0.0",
        port=9999,
    )