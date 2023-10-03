#pip install sqlalchemy pymysql
from sqlalchemy import create_engine, text

# Create the engine
engine = create_engine("mysql+pymysql://admin:Database2023!@database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com/Main")

# Establish a connection
with engine.connect() as connection:
    # Prepare the SQL query
    stmt = text("SELECT * FROM Item LIMIT 10;")

    # Execute the query
    result = connection.execute(stmt)

    # Print the results
    for row in result:
        print(row)
