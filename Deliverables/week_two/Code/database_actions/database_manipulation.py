#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from sqlalchemy.exc import SQLAlchemyError

from database_actions import db


class DatabaseManipulation:
    @staticmethod
    def create_table(statement: str) -> bool:
        try:
            db.session.execute(statement)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False


    @staticmethod
    def add_record(record) -> bool:
        """Add a new record to the database."""
        try:
            db.session.add(record)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False


    @staticmethod
    def check(table, id: int) -> bool:
        """Check if a record with the given ID exists in the table."""
        record = table.query.get(id)
        return record is not None


    @staticmethod
    def execute_command(command: str) -> bool:
        """Execute a raw SQL command."""
        try:
            db.session.execute(command)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False


    @staticmethod
    def drop_all_tables() -> bool:
        password = input('Provide password to delete all tables:')
        if password == 1234:
            try:
                db.drop_all()
                return True
            except SQLAlchemyError:
                return False
