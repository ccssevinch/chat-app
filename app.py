from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    message = data['message']
    message_data = {'username': username, 'message': message}
  
    messages.append(message_data)
   
    emit('receive_message', message_data, broadcast=True)

@socketio.on('connect')
def handle_connect():
    for message in messages:
        emit('receive_message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
