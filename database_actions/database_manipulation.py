import mysql.connector


class DatabaseActions:
    def __init__(self):
        connection = mysql.connector.connect(
            host='database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com',
            user='admin',
            password='Database2023!',
            database='Main'
        )

        self.cursor = connection.cursor()


    def insert(self, table_name: str, columns: list, values: list) -> None:
        """
        Takes the name of a table and a list of values of a row and inserts it into the given table.
        
        Args:
            table_name: The name of the table.
            columns: The list of columns to which the data will be added.
            values: The list of variables to be set as values of respective columns in the row added to the table.
        """""

        data = f"({', '.join(values)})"

        self.cursor.execute(f"INSERT INTO {table_name}({columns}) VALUES {data}")
