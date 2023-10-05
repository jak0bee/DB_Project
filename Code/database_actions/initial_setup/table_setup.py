import mysql.connector


connection = mysql.connector.connect(
    host='database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com',
    user='admin',
    password='Database2023!',
    database='Main'
)

cursor = connection.cursor()

################################################################################

cursor.execute("""
CREATE TABLE Class
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20)
);

CREATE TABLE Event
(
    Id        SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name      VARCHAR(20),
    StartDate DATETIME,
    Duration  DECIMAL(9, 5)
);

CREATE TABLE Achievement
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20) NOT NULL
);

CREATE TABLE Race
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20) NOT NULL
);

CREATE TABLE Ability
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL
);

CREATE TABLE Talent
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL
);

CREATE TABLE Team
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL
);

CREATE TABLE Reward
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name SMALLINT NOT NULL
);

CREATE TABLE Objective
(
    Id   SMALLINT     NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Difficulty
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(20)
);

CREATE TABLE GuildCategory
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE SkillTree
(
    Id        SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    AbilityId SMALLINT,
    TalentId  SMALLINT,
    FOREIGN KEY (AbilityId) REFERENCES Ability (Id),
    FOREIGN KEY (TalentId) REFERENCES Talent (Id)
);

CREATE TABLE Player
(
    Id          SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name        VARCHAR(20) NOT NULL,
    HP          SMALLINT    NOT NULL DEFAULT 100,
    RaceId      SMALLINT    NOT NULL,
    SkillTreeId SMALLINT    NOT NULL,
    ClassId     SMALLINT    NOT NULL,
    Coins       SMALLINT             DEFAULT 0,
    FOREIGN KEY (RaceId) REFERENCES Race (Id),
    FOREIGN KEY (SkillTreeId) REFERENCES SkillTree (Id),
    FOREIGN KEY (ClassId) REFERENCES Class (Id)
);

CREATE TABLE Guild
(
    Id              SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name            VARCHAR(50) NOT NULL,
    GuildCategoryId SMALLINT    NOT NULL,
    FOREIGN KEY (GuildCategoryId) REFERENCES GuildCategory (Id)
);

CREATE TABLE Quest
(
    Id               SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name             VARCHAR(30) NOT NULL,
    RewardId         SMALLINT,
    ObjectiveId      SMALLINT    NOT NULL,
    CompletedAsATeam BOOLEAN     NOT NULL,
    FOREIGN KEY (RewardId) REFERENCES Reward (Id),
    FOREIGN KEY (ObjectiveId) REFERENCES Objective (Id)
);

CREATE TABLE TeamRole
(
    Id     SMALLINT    NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name   VARCHAR(30) NOT NULL,
    TeamId SMALLINT    NOT NULL,
    FOREIGN KEY (TeamId) REFERENCES Team (Id)
);

CREATE TABLE Tables
(
    Id        SMALLINT    NOT NULL AUTO_INCREMENT,
    TableName VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);

CREATE TABLE Inventory
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT,
    OwnerId      SMALLINT NOT NULL,
    OwnerTableId SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (OwnerTableId) REFERENCES Tables (Id)
);

CREATE TABLE ActionHouse
(
    Id           SMALLINT    NOT NULL AUTO_INCREMENT,
    Name         VARCHAR(20) NOT NULL,
    BuyModifier  SMALLINT    NOT NULL,
    SellModifier SMALLINT    NOT NULL,
    PRIMARY KEY (Id)
);

CREATE TABLE NPCRole
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Role VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);

CREATE TABLE NPC
(
    Id         SMALLINT NOT NULL AUTO_INCREMENT,
    HP         SMALLINT NOT NULL,
    RoleId     SMALLINT,
    IsHostile  BOOLEAN  NOT NULL,
    BaseDamage DOUBLE   NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (RoleId) REFERENCES NPCRole (Id)
);

CREATE TABLE ItemEffect
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20),
    PRIMARY KEY (Id)
);

CREATE TABLE ItemCategory
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20),
    PRIMARY KEY (Id)
);

CREATE TABLE Rarity
(
    Id    SMALLINT    NOT NULL AUTO_INCREMENT,
    Name  VARCHAR(20) NOT NULL,
    Color VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);

CREATE TABLE Item
(
    Id             SMALLINT NOT NULL AUTO_INCREMENT,
    Name           VARCHAR(20),
    ItemCategoryId SMALLINT NOT NULL,
    RarityId       SMALLINT NOT NULl,
    Cost           SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (ItemCategoryId) REFERENCES ItemCategory (Id),
    FOREIGN KEY (RarityId) REFERENCES Rarity (Id)
);

CREATE TABLE ItemXItemEffect
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT,
    ItemId       SMALLINT,
    ItemEffectId SMALLINT,
    Modifier     SMALLINT,
    PRIMARY KEY (Id),
    FOREIGN KEY (ItemId) REFERENCES Item (Id),
    FOREIGN KEY (ItemEffectId) REFERENCES ItemEffect (Id)
);

CREATE TABLE BlueprintXItemNeeded
(
    Id              SMALLINT NOT NULL AUTO_INCREMENT,
    BlueprintItemId SMALLINT NOT NULL,
    ItemNeededId    SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (BlueprintItemId) REFERENCES Item (Id),
    FOREIGN KEY (ItemNeededId) REFERENCES Item (Id)
);

CREATE TABLE Crafting
(
    Id              SMALLINT NOT NULL AUTO_INCREMENT,
    BlueprintItemId SMALLINT NOT NULL,
    ResultItemId    SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (BlueprintItemId) REFERENCES Item (Id),
    FOREIGN KEY (ResultItemId) REFERENCES Item (Id)

);

CREATE TABLE Skin
(
    Id     SMALLINT    NOT NULL AUTO_INCREMENT,
    Name   VARCHAR(20) NOT NULL,
    ItemId SMALLINT    NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (ItemId) REFERENCES Item (Id)
);

CREATE TABLE InventoryXItem
(
    Id          SMALLINT NOT NULL AUTO_INCREMENT,
    InventoryId SMALLINT NOT NULL,
    ItemId      SMALLINT NOT NULL,
    IsEquipped  BOOLEAN  NOT NULL,
    Count       SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (ItemId) REFERENCES Item (Id),
    FOREIGN KEY (InventoryId) REFERENCES Inventory (Id)
);

CREATE TABLE EquippedSkin
(
    Id               SMALLINT NOT NULL AUTO_INCREMENT,
    SkinId           SMALLINT NOT NULL,
    InventoryXItemId SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (InventoryXItemId) REFERENCES InventoryXItem (Id),
    FOREIGN KEY (SkinId) REFERENCES Skin (Id)
);

CREATE TABLE Economy
(
    CoinValue SMALLINT NOT NULL
);

CREATE TABLE Kingdom
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);

CREATE TABLE PlayerCustomization
(
    Id               SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PlayerId         SMALLINT NOT NULL,
    OutfitItemId     SMALLINT NOT NULL,
    WeaponSkinItemId SMALLINT NOT NULL,
    EmoteItemId      SMALLINT NOT NULL,
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);

CREATE TABLE TradeOffer
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FromPlayerId SMALLINT NOT NULL,
    ToPlayerId   SMALLINT NOT NULL,
    ItemId       SMALLINT NOT NULL,
    Price        SMALLINT NOT NULL,
    FOREIGN KEY (FromPlayerId) REFERENCES Player (Id),
    FOREIGN KEY (ToPlayerId) REFERENCES Player (Id)
);

CREATE TABLE EventCondition
(
    Id            SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    AchievementId SMALLINT NOT NULL,
    EventId       SMALLINT NOT NULL,
    FOREIGN KEY (AchievementId) REFERENCES Achievement (Id),
    FOREIGN KEY (EventId) REFERENCES Event (Id)
);

CREATE TABLE PlayerXAchievement
(
    Id            SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    AchievementId SMALLINT NOT NULL,
    PlayerId      SMALLINT NOT NULL,
    Date          DATETIME NOT NULL,
    FOREIGN KEY (AchievementId) REFERENCES Achievement (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);

CREATE TABLE TeamXPlayerXRole
(
    Id         SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PlayerId   SMALLINT NOT NULL,
    TeamRoleId SMALLINT NOT NULL,
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (TeamRoleId) REFERENCES TeamRole (Id)
);

CREATE TABLE ObjectiveXQuest
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ObjectiveId  SMALLINT NOT NULL,
    QuestId      SMALLINT NOT NULL,
    IsCurrent    BOOLEAN  NOT NULL,
    PlayerId     SMALLINT NOT NULL,
    DifficultyId SMALLINT NOT NULL,
    FOREIGN KEY (ObjectiveId) REFERENCES Objective (Id),
    FOREIGN KEY (QuestId) REFERENCES Quest (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (DifficultyId) REFERENCES Difficulty (Id)
);

CREATE TABLE PlayerAnalytics
(
    Id                 SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PlayerId           SMALLINT NOT NULL,
    HoursPlayed        DOUBLE   NOT NULL,
    NumberOfDeaths     SMALLINT NOT NULL,
    ItemsCrafted       SMALLINT NOT NULL,
    NPCEncountered     SMALLINT NOT NULL,
    PlayersEncountered SMALLINT NOT NULL,
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);

CREATE TABLE GuildXPlayer
(
    Id       SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PlayerId SMALLINT NOT NULL,
    GuildId  SMALLINT NOT NULL,
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (GuildId) REFERENCES Guild (Id)
);
""")
