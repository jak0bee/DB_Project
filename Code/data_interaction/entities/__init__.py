#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from data_interaction.entities.entity_objects import *


entity_to_class_mapping = {
    'Player': Player,
    'Guild': Guild,
    'Npc': Npc,
    'Question': Question,
    'Enemy': Enemy,
    'Item': Item,
    'SpecialEvent': SpecialEvent,
    'Team': Team
}

guild_register = dict()
