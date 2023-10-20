#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from flask_marshmallow import Marshmallow
from flask_sqlalchemy.model import Model

from database_actions import app


def entry_to_dict(entry: Model) -> dict:
    """
    Turns an object extending Model from flask_sqlalchemy into a dictionary.
    """


    class AutoSchema(Marshmallow(app).SQLAlchemyAutoSchema):
        class Meta:
            model = type(entry)


    schema = AutoSchema()
    return schema.dump(entry)
