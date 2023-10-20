#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
import json
my_json = "{'id':24,'item_name':'RingoftheSages','item_type':'Potion'}"
tmp = json.loads(my_json.replace('\'', '"'))
print(tmp)
print(type(tmp))