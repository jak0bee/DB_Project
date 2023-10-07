entity_types = set()

with open("../../../Resources/generated_entities.txt", 'r') as file:
    for line in file.readlines():
        if line.startswith('---'):
            entity_types.add(line.split(' ')[1])

print(entity_types)
