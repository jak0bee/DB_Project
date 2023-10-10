from database_actions.data.entities.entities import load_guild
from database_actions.database_manipulation import DatabaseManipulation


def load_statements() -> list:
    with open("../../../Resources/generated_entities.txt", 'r') as file:
        data = file.readlines()

    for i in range(len(data)):
        data[i] = data[i].strip()

    result = list()
    for i in range(len(data)):
        if data[i].startswith('---'):
            table = data[i].strip('---').strip()
            columns = list()
            values = list()
            while data[i + 1] or data[i + 2]:
                i += 1
                if data[i]:
                    c, v = [e.strip('"') for e in data[i].split('=')]
                    columns.append(c)
                    if not v.strip("'").isdigit() and not (
                            v.count('.') == 1 and v.strip("'").replace('.', '').isdigit()):
                        v = v.strip("'")
                    values.append(v)

            result.append([table, columns, values])

    return result


def edit_entries(entries: list) -> None:
    for e in entries:
        if e[0] == 'Npc':
            e[1].append('npc_type')
            e[2].append('Standard')
        if e[0] == 'Vendor':
            e[0] = 'Npc'
            e[1].append('npc_type')
            e[2].append('Vendor')

    for e in entries:
        if e[0] == 'Player' or e[0] == 'Npc':
            f_index = e[1].index('first_name')
            f_name = e[2][f_index]
            l_index = e[1].index('last_name')
            l_name = e[2][l_index]
            name = f"""{e[2][f_index].strip("'")} {e[2][l_index].strip("'")}"""
            e[1].remove('first_name')
            e[1].remove('last_name')
            e[2].remove(f_name)
            e[2].remove(l_name)
            if e[0] == 'Player':
                e[1].append('player_name')
            else:
                e[1].append('npc_name')
            e[2].append(name)

    guild_data = dict()
    for e in entries:
        if e[0] == 'Guild':
            if e[2][e[1].index('guild_name')] not in guild_data:
                guild_data[e[2][e[1].index('guild_name')]] = e[2][e[1].index('id')]

    for e in entries:
        if e[0] == 'Player':
            index = e[1].index('guild_name')
            entries[entries.index(e)][1][index] = 'guild_id'
            if e[2][index] not in guild_data:
                entries.remove(e)
            else:
                entries[entries.index(e)][2][index] = guild_data[e[2][index]]


statements = load_statements()
edit_entries(statements)

database_manipulation = DatabaseManipulation()

for statement in statements:
    for e in statement[2]:
        if "'" in e[1:-1]:
            statement[2][statement[2].index(e)] = statement[2][statement[2].index(e)].replace("'", "''")
    if statement[0] == 'SpecialEvent' or statement[0] == 'Player':
        for e in statement[1]:
            if e == 'start_time' or e == 'last_login':
                statement[2][statement[1].index(e)] = statement[2][statement[1].index(e)].replace('T', ' ')

for statement in statements:
    if statement[0] == 'Guild':
        database_manipulation.insert(statement[0], statement[1], statement[2])

for statement in statements:
    if statement[0] != 'Guild':
        database_manipulation.insert(statement[0], statement[1], statement[2])
