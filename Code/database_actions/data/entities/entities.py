from sqlalchemy import text


def load_guild(data):
    statement = text("INSERT INTO Guild(id, guild_name, guild_category, leader, number_of_members, founded_year) VALUES (:id, :guild_name, :guild_category, :leader, :number_of_members, :founded_year)")

    bound_statement = statement.bindparams(
        id=data[2][0],
        guild_name=data[2][1],
        guild_category=data[2][2],
        leader=data[2][3],
        number_of_members=data[2][4],
        founded_year=data[2][5]
    )

    return bound_statement
