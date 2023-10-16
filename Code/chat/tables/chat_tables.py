from chat import db


class ChatSession(db.Model):
    __tablename__ = 'ChatSession'
    session_id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String(50), nullable=False)
    session_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
