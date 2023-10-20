#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
def separate_statements(text: str) -> None:
    statements = text.split(';')
    print('[')
    for e in statements[:len(statements) - 1]:
        comma = ',' if e is not statements[-2] else ''
        print(f'"""{e.strip()}"""{comma}')
    print(']')
