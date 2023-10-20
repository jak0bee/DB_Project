# Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from flask_socketio import emit, join_room

from database_actions import socket, app


@socket.on('send_message')
def handle_send_message(data):
    sender_id = data['sender_id']
    session_id = data['session_id']
    message_content = data['message']

    socket.emit('received_message', {'sender_id': sender_id, 'message': message_content}, room=str(session_id))


@socket.on('join')
def on_join(data):
    session_id = data['session_id']
    join_room(str(session_id))
    emit('added_to_chat')


if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
