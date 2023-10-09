from sqlalchemy import create_engine, text
from database_actions import database_url


engine = create_engine(database_url)
connection = engine.connect()

################################################################################

connection.execute(text("""
CREATE TABLE Class
(
    id         SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(20)
);

CREATE TABLE SpecialEvent
(
    id                 SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    special_event_name VARCHAR(20),
    start_date         DATETIME,
    end_date           DATETIME
);

CREATE TABLE Achievement
(
    Id               SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    achievement_name VARCHAR(35) NOT NULL
);

CREATE TABLE Race
(
    id        SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    race_name VARCHAR(20) NOT NULL
);

CREATE TABLE Ability
(
    id           SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ability_name VARCHAR(30) NOT NULL
);

CREATE TABLE Talent
(
    id          SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    talent_name VARCHAR(30) NOT NULL
);

CREATE TABLE Team
(
    id        SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(30) NOT NULL
);

CREATE TABLE Reward
(
    id          SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    reward_name SMALLINT NOT NULL
);

CREATE TABLE Objective
(
    id             SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
    objective_name VARCHAR(100) NOT NULL
);

CREATE TABLE Difficulty
(
    id              SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    difficulty_name VARCHAR(20)
);

CREATE TABLE GuildCategory
(
    id                  SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    guild_category_name VARCHAR(50) NOT NULL
);

CREATE TABLE SkillTree
(
    id         SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ability_id SMALLINT,
    talent_id  SMALLINT,
    FOREIGN KEY (ability_id) REFERENCES Ability (id),
    FOREIGN KEY (talent_id) REFERENCES Talent (id)
);

CREATE TABLE Player
(
    id            SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_name   VARCHAR(50) NOT NULL,
    hitpoints     SMALLINT    NOT NULL DEFAULT 100,
    race_id       SMALLINT    NOT NULL,
    skill_tree_id SMALLINT    NOT NULL,
    class_id      SMALLINT    NOT NULL,
    coins         SMALLINT             DEFAULT 0,
    FOREIGN KEY (race_id) REFERENCES Race (id),
    FOREIGN KEY (skill_tree_id) REFERENCES SkillTree (id),
    FOREIGN KEY (class_id) REFERENCES Class (id)
);

CREATE TABLE Guild
(
    id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    guild_name        VARCHAR(50) NOT NULL,
    guild_category_id SMALLINT    NOT NULL,
    FOREIGN KEY (guild_category_id) REFERENCES GuildCategory (id)
);

CREATE TABLE Quest
(
    id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quest_name        VARCHAR(30) NOT NULL,
    reward_id         SMALLINT,
    objective_id      SMALLINT    NOT NULL,
    completed_as_team BOOLEAN     NOT NULL,
    FOREIGN KEY (reward_id) REFERENCES Reward (id),
    FOREIGN KEY (objective_id) REFERENCES Objective (id)
);

CREATE TABLE TeamRole
(
    id             SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    team_role_name VARCHAR(30) NOT NULL,
    team_id        SMALLINT    NOT NULL,
    FOREIGN KEY (team_id) REFERENCES Team (id)
);

CREATE TABLE Tables
(
    id         SMALLINT    NOT NULL AUTO_INCREMENT,
    table_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Inventory
(
    id             SMALLINT NOT NULL AUTO_INCREMENT,
    owner_id       SMALLINT NOT NULL,
    owner_table_id SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_table_id) REFERENCES Tables (id)
);

CREATE TABLE ActionHouse
(
    id                SMALLINT    NOT NULL AUTO_INCREMENT,
    action_house_name VARCHAR(20) NOT NULL,
    buy_modifier      SMALLINT    NOT NULL,
    sell_modifier     SMALLINT    NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE NPCRole
(
    id            SMALLINT    NOT NULL AUTO_INCREMENT,
    npc_role_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE NPC
(
    id          SMALLINT NOT NULL AUTO_INCREMENT,
    hitpoints   SMALLINT NOT NULL,
    role_id     SMALLINT,
    kis_hostile BOOLEAN  NOT NULL,
    base_damage DOUBLE   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (role_id) REFERENCES NPCRole (id)
);

CREATE TABLE ItemEffect
(
    id             SMALLINT NOT NULL AUTO_INCREMENT,
    item_effect_id VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE ItemCategory
(
    id                 SMALLINT NOT NULL AUTO_INCREMENT,
    item_category_name VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE Rarity
(
    id          SMALLINT    NOT NULL AUTO_INCREMENT,
    rarity_name VARCHAR(20) NOT NULL,
    color       VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Item
(
    id               SMALLINT NOT NULL AUTO_INCREMENT,
    item_name        VARCHAR(20),
    item_category_id SMALLINT NOT NULL,
    rarity_id        SMALLINT NOT NULL,
    cost             SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (item_category_id) REFERENCES ItemCategory (id),
    FOREIGN KEY (rarity_id) REFERENCES Rarity (id)
);

CREATE TABLE ItemXItemEffect
(
    id             SMALLINT NOT NULL AUTO_INCREMENT,
    item_id        SMALLINT,
    item_effect_id SMALLINT,
    modifier       SMALLINT,
    PRIMARY KEY (id),
    FOREIGN KEY (item_id) REFERENCES Item (id),
    FOREIGN KEY (item_effect_id) REFERENCES ItemEffect (id)
);

CREATE TABLE BlueprintXItemNeeded
(
    id                SMALLINT NOT NULL AUTO_INCREMENT,
    blueprint_item_id SMALLINT NOT NULL,
    item_needed_id    SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (blueprint_item_id) REFERENCES Item (id),
    FOREIGN KEY (item_needed_id) REFERENCES Item (id)
);

CREATE TABLE Crafting
(
    id                SMALLINT NOT NULL AUTO_INCREMENT,
    blueprint_item_id SMALLINT NOT NULL,
    result_item_id    SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (blueprint_item_id) REFERENCES Item (id),
    FOREIGN KEY (result_item_id) REFERENCES Item (id)

);

CREATE TABLE Skin
(
    id        SMALLINT    NOT NULL AUTO_INCREMENT,
    skin_name VARCHAR(20) NOT NULL,
    item_id   SMALLINT    NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (item_id) REFERENCES Item (id)
);

CREATE TABLE InventoryXItem
(
    id           SMALLINT NOT NULL AUTO_INCREMENT,
    inventory_id SMALLINT NOT NULL,
    item_id      SMALLINT NOT NULL,
    is_equipped  BOOLEAN  NOT NULL,
    count        SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (item_id) REFERENCES Item (id),
    FOREIGN KEY (inventory_id) REFERENCES Inventory (id)
);

CREATE TABLE EquippedSkin
(
    id                  SMALLINT NOT NULL AUTO_INCREMENT,
    skin_id             SMALLINT NOT NULL,
    inventory_x_item_id SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (inventory_x_item_id) REFERENCES InventoryXItem (id),
    FOREIGN KEY (skin_id) REFERENCES Skin (id)
);

CREATE TABLE Economy
(
    coin_value SMALLINT NOT NULL
);

CREATE TABLE Kingdom
(
    id           SMALLINT    NOT NULL AUTO_INCREMENT,
    kingdom_name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE PlayerCustomization
(
    id                  SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id           SMALLINT NOT NULL,
    outfit_item_id      SMALLINT NOT NULL,
    weapon_skin_item_id SMALLINT NOT NULL,
    emote_item_id       SMALLINT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Player (id)
);

CREATE TABLE TradeOffer
(
    id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    from_player_id SMALLINT NOT NULL,
    to_player_id   SMALLINT NOT NULL,
    item_id        SMALLINT NOT NULL,
    price          SMALLINT NOT NULL,
    FOREIGN KEY (from_player_id) REFERENCES Player (id),
    FOREIGN KEY (to_player_id) REFERENCES Player (id)
);

CREATE TABLE EventCondition
(
    id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    achievement_id SMALLINT NOT NULL,
    event_id       SMALLINT NOT NULL,
    FOREIGN KEY (achievement_id) REFERENCES Achievement (id),
    FOREIGN KEY (event_id) REFERENCES SpecialEvent (id)
);

CREATE TABLE PlayerXAchievement
(
    id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    achievement_id SMALLINT NOT NULL,
    player_id      SMALLINT NOT NULL,
    date           DATETIME NOT NULL,
    FOREIGN KEY (achievement_id) REFERENCES Achievement (id),
    FOREIGN KEY (player_id) REFERENCES Player (id)
);

CREATE TABLE TeamXPlayerXRole
(
    id           SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id    SMALLINT NOT NULL,
    team_role_id SMALLINT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Player (id),
    FOREIGN KEY (team_role_id) REFERENCES TeamRole (id)
);

CREATE TABLE ObjectiveXQuest
(
    id            SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    objective_id  SMALLINT NOT NULL,
    quest_id      SMALLINT NOT NULL,
    is_current    BOOLEAN  NOT NULL,
    player_id     SMALLINT NOT NULL,
    difficulty_id SMALLINT NOT NULL,
    FOREIGN KEY (objective_id) REFERENCES Objective (id),
    FOREIGN KEY (quest_id) REFERENCES Quest (id),
    FOREIGN KEY (player_id) REFERENCES Player (id),
    FOREIGN KEY (difficulty_id) REFERENCES Difficulty (id)
);

CREATE TABLE PlayerAnalytics
(
    id                  SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id           SMALLINT NOT NULL,
    hours_played        DOUBLE   NOT NULL,
    number_of_deaths    SMALLINT NOT NULL,
    items_crafted       SMALLINT NOT NULL,
    npcs_encountered    SMALLINT NOT NULL,
    players_encountered SMALLINT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Player (id)
);

CREATE TABLE GuildXPlayer
(
    id        SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id SMALLINT NOT NULL,
    guild_id  SMALLINT NOT NULL,
    FOREIGN KEY (player_id) REFERENCES Player (id),
    FOREIGN KEY (guild_id) REFERENCES Guild (id)
);
"""))
