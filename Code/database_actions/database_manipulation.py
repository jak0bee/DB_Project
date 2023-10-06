from sqlalchemy import create_engine, text


class DatabaseActions:
    def __init__(self):
        engine = create_engine(
            "mysql+pymysql://admin:Database2023!@database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com/Main")

        self.connection = engine.connect()


    def insert(self, table_name: str, values: list, columns: list) -> None:
        """
        Takes the name of a table and a list of values of a row and inserts it into the given table.

        Args:
            table_name: The name of the table.
            columns: The list of columns to which the data will be added.
            values: The list of variables to be set as values of respective columns in the row added to the table.
        """""

        data = f"({', '.join(values)})"

        self.connection.execute(text(f"INSERT INTO {table_name}({columns}) VALUES {data}"))
