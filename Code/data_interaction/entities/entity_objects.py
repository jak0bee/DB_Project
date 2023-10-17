"""
This module provides classes defining the structure of entities in the game.
Objects of these classes can each represent an entity and help with e.g. importing them to the database.
"""

from sqlalchemy import Column, String, ForeignKey, DateTime, Numeric, SmallInteger
from sqlalchemy.orm import relationship

from database_actions import db


class Enemy(db.Model):
    __tablename__ = 'Enemy'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    enemy_name = Column(String(50), nullable=False)
    enemy_type = Column(String(50))
    hit_points = Column(SmallInteger, nullable=False)
    war_cry = Column(String(100), nullable=False)


class Question(db.Model):
    __tablename__ = 'Question'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    content = Column(String(300), nullable=False)
    choice_options = Column(SmallInteger, nullable=False)
    emotion = Column(SmallInteger, nullable=False)


class Item(db.Model):
    __tablename__ = 'Item'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    item_name = Column(String(40))
    item_category = Column(String(30), nullable=False)
    cost = Column(SmallInteger, default=0)


class Npc(db.Model):
    __tablename__ = 'Npc'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    npc_name = Column(String(50), nullable=False)
    npc_type = Column(String(50), nullable=False)
    npc_role = Column(String(50), nullable=False)
    location = Column(Numeric, nullable=False)


class Player(db.Model):
    __tablename__ = 'Player'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    player_name = Column(String(100), nullable=False)
    hit_points = Column(SmallInteger, default=100)
    race = Column(String(50), nullable=False)
    player_class = Column(String(50), nullable=False, name="class")
    guild_id = Column(SmallInteger, ForeignKey('Guild.id'))
    coins = Column(SmallInteger, default=0)
    last_login = Column(DateTime)

    guild = relationship("Guild", back_populates="players")


class Guild(db.Model):
    __tablename__ = 'Guild'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    guild_name = Column(String(50), nullable=False)
    guild_category = Column(String(50), nullable=False)
    leader = Column(String(30), nullable=False)
    number_of_members = Column(SmallInteger, nullable=False)
    founded_year = Column(SmallInteger, nullable=False)

    players = relationship("Player", back_populates="guild")


class Team(db.Model):
    __tablename__ = 'Team'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    team_name = Column(String(30), nullable=False)
    kingdom = Column(String(50), nullable=False)
    number_of_members = Column(SmallInteger, default=0)


class SpecialEvent(db.Model):
    __tablename__ = 'SpecialEvent'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    special_event_name = Column(String(50), nullable=False)
    time = Column(SmallInteger, nullable=False)
