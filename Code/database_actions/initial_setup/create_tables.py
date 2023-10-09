from database_actions.database_manipulation import DatabaseManipulation
from database_actions.initial_setup import table_creation_statements


database_manipulation = DatabaseManipulation()
for statement in table_creation_statements:
    database_manipulation.create_table(statement)
