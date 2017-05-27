from flask import Flask
from flask_socketio import SocketIO


## Instanciate Flask (Static files and REST API)
app = Flask(__name__)
## Instanciate SocketIO (Websockets, used for events) on top of it
socketio = SocketIO(app)


@socketio.on('testEvent')
def test_event(_=None):
    print "Got test event"

@socketio.on('testEventWithException')
def test_event_with_exception(_=None):
    print "Got test event, throwing exception NOW"
    raise Exception()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
