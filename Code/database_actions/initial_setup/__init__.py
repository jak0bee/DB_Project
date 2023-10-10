table_creation_statements = [
    """CREATE TABLE SpecialEvent
    (
        id                 SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        special_event_name VARCHAR(50) NOT NULL,
        time               SMALLINT    NOT NULL
    )""",
    """CREATE TABLE Achievement
    (
        id               SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        achievement_name VARCHAR(35) NOT NULL UNIQUE
    )""",
    """CREATE TABLE Ability
    (
        id           SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        ability_name VARCHAR(30) NOT NULL UNIQUE
    )""",
    """CREATE TABLE Talent
    (
        id          SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        talent_name VARCHAR(30) NOT NULL UNIQUE
    )""",
    """CREATE TABLE Team
    (
        id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        team_name         VARCHAR(30) NOT NULL,
        kingdom           VARCHAR(50) NOT NULL,
        number_of_members SMALLINT    NOT NULL DEFAULT 0
    )""",
    """CREATE TABLE Reward
    (
        id          SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        reward_name SMALLINT NOT NULL UNIQUE
    )""",
    """CREATE TABLE Objective
    (
        id             SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
        objective_name VARCHAR(100) NOT NULL
    )""",
    """CREATE TABLE Difficulty
    (
        id              SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        difficulty_name VARCHAR(20) UNIQUE
    )""",
    """CREATE TABLE Guild
    (
        id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        guild_name        VARCHAR(50) NOT NULL,
        guild_category    VARCHAR(50) NOT NULL,
        leader            VARCHAR(30) NOT NULL,
        number_of_members SMALLINT    NOT NULL,
        founded_year      SMALLINT    NOT NULL
    )
    """,
    """CREATE TABLE Player
    (
        id          SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_name VARCHAR(100) NOT NULL UNIQUE,
        hit_points  SMALLINT     NOT NULL DEFAULT 100,
        race        VARCHAR(50)  NOT NULL,
        class       VARCHAR(50)  NOT NULL,
        guild_id    SMALLINT,
        coins       SMALLINT              DEFAULT 0,
        last_login  DATETIME,
        FOREIGN KEY (guild_id) REFERENCES Guild(id)
    )""",
    """CREATE TABLE SkillTree
    (
        id         SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_id  SMALLINT NOT NULL ,
        ability_id SMALLINT,
        talent_id  SMALLINT,
        FOREIGN KEY (ability_id) REFERENCES Ability (id),
        FOREIGN KEY (talent_id) REFERENCES Talent (id),
        FOREIGN KEY (player_id) REFERENCES Player (id)
    )""",
    """CREATE TABLE Quest
    (
        id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        quest_name        VARCHAR(30) NOT NULL UNIQUE,
        reward_id         SMALLINT,
        objective_id      SMALLINT    NOT NULL,
        completed_as_team BOOLEAN     NOT NULL,
        FOREIGN KEY (reward_id) REFERENCES Reward (id),
        FOREIGN KEY (objective_id) REFERENCES Objective (id)
    )""",
    """CREATE TABLE TeamRole
    (
        id             SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        team_role_name VARCHAR(30) NOT NULL UNIQUE,
        team_id        SMALLINT    NOT NULL,
        FOREIGN KEY (team_id) REFERENCES Team (id)
    )""",
    """CREATE TABLE Tables
    (
        id         SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        table_name VARCHAR(20) NOT NULL
    )""",
    """CREATE TABLE Inventory
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        owner_id       SMALLINT NOT NULL,
        owner_table_id SMALLINT NOT NULL,
        FOREIGN KEY (owner_table_id) REFERENCES Tables (id)
    )""",
    """CREATE TABLE ActionHouse
    (
        id                SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        action_house_name VARCHAR(20) NOT NULL,
        buy_modifier      SMALLINT    NOT NULL,
        sell_modifier     SMALLINT    NOT NULL
    )""",
    """CREATE TABLE Npc
    (
        id       SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        npc_name VARCHAR(50) NOT NULL,
        npc_type VARCHAR(50) NOT NULL,
        npc_role VARCHAR(50) NOT NULL,
        location NUMERIC     NOT NULL
    )""",
    """CREATE TABLE ItemEffect
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        item_effect_id VARCHAR(20)
    )""",
    """CREATE TABLE Item
    (
        id               SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        item_name        VARCHAR(40),
        item_category    VARCHAR(30) NOT NULL,
        cost             SMALLINT NOT NULL DEFAULT 0
    )""",
    """CREATE TABLE ItemXItemEffect
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        item_id        SMALLINT,
        item_effect_id SMALLINT,
        modifier       SMALLINT,
        FOREIGN KEY (item_id) REFERENCES Item (id),
        FOREIGN KEY (item_effect_id) REFERENCES ItemEffect (id)
    )""",
    """CREATE TABLE BlueprintXItemNeeded
    (
        id                SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        blueprint_item_id SMALLINT NOT NULL,
        item_needed_id    SMALLINT NOT NULL,
        FOREIGN KEY (blueprint_item_id) REFERENCES Item (id),
        FOREIGN KEY (item_needed_id) REFERENCES Item (id)
    )""",
    """CREATE TABLE Crafting
    (
        id                SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        blueprint_item_id SMALLINT NOT NULL,
        result_item_id    SMALLINT NOT NULL,
        FOREIGN KEY (blueprint_item_id) REFERENCES Item (id),
        FOREIGN KEY (result_item_id) REFERENCES Item (id)
    
    )""",
    """CREATE TABLE Skin
    (
        id        SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        skin_name VARCHAR(20) NOT NULL UNIQUE,
        item_id   SMALLINT    NOT NULL,
        FOREIGN KEY (item_id) REFERENCES Item (id)
    )""",
    """CREATE TABLE InventoryXItem
    (
        id           SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        inventory_id SMALLINT NOT NULL,
        item_id      SMALLINT NOT NULL,
        is_equipped  BOOLEAN  NOT NULL,
        count        SMALLINT NOT NULL,
        FOREIGN KEY (item_id) REFERENCES Item (id),
        FOREIGN KEY (inventory_id) REFERENCES Inventory (id)
    )""",
    """CREATE TABLE EquippedSkin
    (
        id                  SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        skin_id             SMALLINT NOT NULL,
        inventory_x_item_id SMALLINT NOT NULL,
        FOREIGN KEY (inventory_x_item_id) REFERENCES InventoryXItem (id),
        FOREIGN KEY (skin_id) REFERENCES Skin (id)
    )""",
    """CREATE TABLE Economy
    (
        coin_value SMALLINT NOT NULL
    )""",
    """CREATE TABLE PlayerCustomization
    (
        id                  SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_id           SMALLINT NOT NULL,
        outfit_item_id      SMALLINT NOT NULL,
        weapon_skin_item_id SMALLINT NOT NULL,
        emote_item_id       SMALLINT NOT NULL,
        FOREIGN KEY (player_id) REFERENCES Player (id)
    )""",
    """CREATE TABLE TradeOffer
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        from_player_id SMALLINT NOT NULL,
        to_player_id   SMALLINT NOT NULL,
        item_id        SMALLINT NOT NULL,
        price          SMALLINT NOT NULL,
        FOREIGN KEY (from_player_id) REFERENCES Player (id),
        FOREIGN KEY (to_player_id) REFERENCES Player (id)
    )""",
    """CREATE TABLE EventCondition
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        achievement_id SMALLINT NOT NULL,
        event_id       SMALLINT NOT NULL,
        FOREIGN KEY (achievement_id) REFERENCES Achievement (id),
        FOREIGN KEY (event_id) REFERENCES SpecialEvent (id)
    )""",
    """CREATE TABLE PlayerXAchievement
    (
        id             SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        achievement_id SMALLINT NOT NULL,
        player_id      SMALLINT NOT NULL,
        date           DATETIME NOT NULL,
        FOREIGN KEY (achievement_id) REFERENCES Achievement (id),
        FOREIGN KEY (player_id) REFERENCES Player (id)
    )""",
    """CREATE TABLE TeamXPlayerXRole
    (
        id           SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_id    SMALLINT NOT NULL,
        team_role_id SMALLINT NOT NULL,
        FOREIGN KEY (player_id) REFERENCES Player (id),
        FOREIGN KEY (team_role_id) REFERENCES TeamRole (id)
    )""",
    """CREATE TABLE ObjectiveXQuest
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
    )""",
    """CREATE TABLE PlayerAnalytics
    (
        id                  SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_id           SMALLINT NOT NULL,
        hours_played        DOUBLE   NOT NULL,
        number_of_deaths    SMALLINT NOT NULL,
        items_crafted       SMALLINT NOT NULL,
        npcs_encountered    SMALLINT NOT NULL,
        players_encountered SMALLINT NOT NULL,
        FOREIGN KEY (player_id) REFERENCES Player (id)
    )""",
    """CREATE TABLE Question
    (
        id             SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
        content        VARCHAR(300) NOT NULL,
        choice_options SMALLINT     NOT NULL,
        emotion        SMALLINT     NOT NULL
    )""",
    """CREATE TABLE Enemy
    (
        id   SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
        enemy_name VARCHAR(50)  NOT NULL,
        enemy_type VARCHAR(50),
        hit_points SMALLINT     NOT NULL,
        war_cry    VARCHAR(100) NOT NULL
    )""",
    """CREATE TABLE Event
    (
        id                     SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        event_type             VARCHAR(20) NOT NULL,
        timestamp              DATETIME    NOT NULL,
        entity1_id             SMALLINT    NOT NULL,
        entity1_type           VARCHAR(20) NOT NULL,
        entity2_id             SMALLINT    NOT NULL,
        entity2_type           VARCHAR(20) NOT NULL,
        value                  VARCHAR(20) NOT NULL,
        additional_entity_id   SMALLINT,
        additional_entity_type VARCHAR(20)
    )""",
    """CREATE TABLE Dialogue
    (
        id             SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
        content        VARCHAR(50) NOT NULL,
        choice_options SMALLINT    NOT NULL,
        emotion        SMALLINT
    )"""
]
