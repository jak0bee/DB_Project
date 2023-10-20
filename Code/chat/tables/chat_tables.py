# Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from database_actions import db


class ChatSession(db.Model):
    __tablename__ = 'ChatSession'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    session_name = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    messages = db.relationship('ChatMessage', backref='chat_session', lazy=True)
    members = db.relationship('GroupChatMember', backref='chat_session', lazy=True)


class ChatMessage(db.Model):
    __tablename__ = 'ChatMessage'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    session_id = db.Column(db.SmallInteger, db.ForeignKey('ChatSession.id'), nullable=False)
    sender_id = db.Column(db.SmallInteger, db.ForeignKey('Player.id'), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=db.func.current_timestamp())


class GroupChatMember(db.Model):
    __tablename__ = 'GroupChatMember'

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    session_id = db.Column(db.SmallInteger, db.ForeignKey('ChatSession.id'), nullable=False)
    player_id = db.Column(db.SmallInteger, db.ForeignKey('Player.id'), nullable=False)
