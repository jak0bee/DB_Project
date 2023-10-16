"""
This module provides classes defining the structure of entities in the game.
Objects of these classes can each represent an entity and help with e.g. importing them to the database.
"""

from data_interaction.entities import guild_register


class Player:
    # validation_rules = {
    #     'id': int,
    #     'first_name': str,
    #     'last_name': str,
    #     'race': str,
    #     'class': str,
    #     'guild_name': str,
    #     'last_login': str
    # }


    def __init__(self, id_number, f_name, l_name, race, player_class, guild_name, last_login, coins=0, hit_points=100):
        self.id = id_number
        self.player_name = ' '.join([f_name, l_name])
        self.hit_points = hit_points
        self.race = race
        self.player_class = player_class
        self.guild_id = guild_register[guild_name]
        self.coins = coins
        self.last_login = last_login


class Guild:
    def __init__(self, id_number, guild_name, leader, number_of_members, founded_year):
        self.id = id_number
        self.guild_name = guild_name
        self.leader = leader
        self.number_of_members = number_of_members
        self.founded_year = founded_year


class Npc:
    def __init__(self, id_number, npc_name, npc_type, npc_role, location):
        self.id = id_number
        self.npc_name = npc_name
        self.npc_type = npc_type
        self.npc_role = npc_role
        self.location = location


class Question:
    def __init__(self, id_number, content, choice_options, emotion):
        self.id = id_number
        self.content = content
        self.choice_options = choice_options
        self.emotion = emotion


class Enemy:
    def __init__(self, id_number, enemy_name, enemy_type, hit_points, war_cry):
        self.id = id_number
        self.enemy_name = enemy_name
        self.enemy_type = enemy_type
        self.hit_points = hit_points
        self.war_cry = war_cry


class Item:
    def __init__(self, id_number, item_name, item_category, cost):
        self.id = id_number
        self.item_name = item_name
        self.item_category = item_category
        self.cost = cost


class SpecialEvent:
    def __init__(self, id_number, special_event_name, time):
        self.id = id_number
        self.special_event_name = special_event_name
        self.time = time


class Team:
    def __init__(self, id_number, team_name, kingdom, number_of_members):
        self.id = id_number
        self.team_name = team_name
        self.kingdom = kingdom
        self.number_of_members = number_of_members
