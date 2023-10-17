from flask import request, jsonify

from chat.tables.chat_tables import ChatSession, ChatMessage, GroupChatMember
from database_actions import app, db, socket
from utils.entry_to_dictionary import entry_to_dict


@app.route('/chat/session', methods=['POST'])
def create_chat_session():
    data = request.json
    session_type = data.get('session_type')
    session_name = data.get('session_name', None)  # This can be optional

    new_session = ChatSession(session_type=session_type, session_name=session_name)
    db.session.add(new_session)
    db.session.commit()

    return jsonify({"message": "Chat session created!", "session_id": new_session.id}), 201


@app.route('/chat/message', methods=['POST'])
def send_message():
    data = request.json
    session_id = data.get('session_id')
    sender_id = data.get('sender_id')
    message_text = data.get('message_text')

    new_message = ChatMessage(session_id=session_id, sender_id=sender_id, message_text=message_text)
    db.session.add(new_message)
    db.session.commit()

    return jsonify({"message": "Message sent!", "message_id": new_message.id}), 201


@app.route('/chat/messages/<int:session_id>', methods=['GET'])
def fetch_messages(session_id):
    messages = ChatMessage.query.filter_by(session_id=session_id).all()
    return jsonify([message.serialize() for message in messages]), 200


@app.route('/chat/group/<int:session_id>/add', methods=['POST'])
def add_member_to_group(session_id):
    data = request.json
    player_id = data.get('player_id')

    new_member = GroupChatMember(session_id=session_id, player_id=player_id)
    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Member added!", "member_id": new_member.member_id}), 201


@app.route('/chat/group/<int:session_id>/remove', methods=['POST'])
def remove_member_from_group(session_id):
    data = request.json
    player_id = data.get('player_id')

    member = GroupChatMember.query.filter_by(session_id=session_id, player_id=player_id).first()
    if member:
        db.session.delete(member)
        db.session.commit()
        return jsonify({"message": "Member removed!"}), 200
    return jsonify({"message": "Member not found!"}), 404


@app.route('/chat/group/<int:session_id>/members', methods=['GET'])
def fetch_group_members(session_id):
    members = GroupChatMember.query.filter_by(session_id=session_id).all()
    return jsonify([entry_to_dict(member) for member in members]), 200


@app.route('/chat/sessions/<int:player_id>', methods=['GET'])
def fetch_chat_sessions(player_id):
    sessions = db.session.query(ChatSession).join(GroupChatMember).filter(GroupChatMember.player_id == player_id).all()
    return jsonify([entry_to_dict(session) for session in sessions]), 200


@socket.on('send_message')
def handle_send_message(data):
    # Save the message to the database, if needed
    # Broadcast the message to all connected clients or specific rooms
    socket.emit('receive_message', data, broadcast=True)
