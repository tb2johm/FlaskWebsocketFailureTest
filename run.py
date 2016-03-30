from flask import Flask, render_template, request
from flask.ext.socketio import SocketIO
from main_page import main_pages
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.debug = False
app.secret_key = 'testesteste'

app.register_blueprint(main_pages, url_prefix="/")

sio = SocketIO(app, async_mode="eventlet", transports=['xhr-polling'])


@main_pages.route('/')
def show_main():
    return render_template("index.html")


@sio.on('connect', namespace='/sio')
def sio_connect():
    print("#### connect")
    pass


@sio.on('request', namespace='/sio')
def sio_request(message):
    print("#### request:", message)
    sio.emit('pong', "null")
    sio.emit('response', message, room=request.sid, namespace="/sio")
    print("#### response sent")

if __name__ == "__main__":
    sio.run(app, host="localhost", port=3030, debug=True, use_reloader=False)