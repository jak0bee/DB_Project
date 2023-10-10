from sqlalchemy import create_engine, text, MetaData
from database_actions import database_url
from sqlalchemy.exc import ProgrammingError,OperationalError


class DatabaseManipulation:
    def __init__(self):
        self.engine = create_engine(database_url)
        self.connection = self.engine.connect()


    def create_table(self, statement: str) -> None:
        self.connection.execute(text(statement))


    def execute_command(self, command: text) -> None:
        self.connection.execute(command)


    def insert(self, table_name: str, columns: list, values: list) -> None:
        """
        Takes the name of a table and a list of values of a row and inserts it into the given table.

        Args:
            table_name: The name of the table.
            columns: The list of columns to which the data will be added.
            values: The list of variables to be set as values of respective columns in the row added to the table.
        """

        for v in values:
            if not (v.isdigit() or not v.count('.') == 1 and v.replace('.', '').isdigit()):
                if v == "null":
                    values[values.index(v)] = "null"
                else:
                    values[values.index(v)] = f"'{v}'"

        cols = f"({', '.join(columns)})"
        vals = f"({', '.join(values)})"
        query = f"INSERT INTO {table_name} {cols} VALUES {vals};"
        self.connection.execute(text(query))
        print(query)

    def check(self, table_name: str, id: int) -> bool:
        # Format table name (assuming only the first letter should be uppercase)
        table_name = table_name[0].upper() + table_name[1:].lower()

        # Construct the SQL query to check for the ID in the specified table
        query_string = f"SELECT * FROM {table_name} WHERE Id = {id} LIMIT 1"
        query = text(query_string)


        # Execute the query
        result = self.connection.execute(query).fetchone()

        # If the result is not None, the ID exists in the table
        return result is not None


    def drop_all_tables(self) -> None:
        meta = MetaData()
        meta.reflect(bind=self.engine)

        with self.engine.begin() as connection:
            connection.execute(text("SET FOREIGN_KEY_CHECKS=0"))

        meta.drop_all(self.engine)

        with self.engine.begin() as connection:
            connection.execute(text("SET FOREIGN_KEY_CHECKS=1"))
