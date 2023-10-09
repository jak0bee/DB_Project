from sqlalchemy import create_engine, text, MetaData
from database_actions import database_url


class DatabaseManipulation:
    def __init__(self):
        self.engine = create_engine(database_url)
        self.connection = self.engine.connect()


    def create_table(self, statement: str) -> None:
        self.connection.execute(text(statement))


    def insert(self, table_name: str, values: list, columns: list) -> None:
        """
        Takes the name of a table and a list of values of a row and inserts it into the given table.

        Args:
            table_name: The name of the table.
            columns: The list of columns to which the data will be added.
            values: The list of variables to be set as values of respective columns in the row added to the table.
        """

        data = f"({', '.join(values)})"

        self.connection.execute(text(f"INSERT INTO {table_name}({columns}) VALUES {data}"))


    def drop_all_tables(self) -> None:
        meta = MetaData()
        meta.reflect(bind=self.engine)

        with self.engine.begin() as connection:
            connection.execute(text("SET FOREIGN_KEY_CHECKS=0"))

        meta.drop_all(self.engine)

        with self.engine.begin() as connection:
            connection.execute(text("SET FOREIGN_KEY_CHECKS=1"))
