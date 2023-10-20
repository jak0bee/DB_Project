#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from database_actions import socket, app


if __name__ == '__main__':
    socket.run(app, allow_unsafe_werkzeug=True)
