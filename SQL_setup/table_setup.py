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
    Id      SMALLINT NOT NULL AUTO_INCREMENT,
    Name    VARCHAR(20),
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Event
(
    Id        SMALLINT NOT NULL AUTO_INCREMENT,
    Name      VARCHAR(20),
    StartDate VARCHAR(19),
    Duration  SMALLINT,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Achievement
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE EventCondition
(
    Id            SMALLINT NOT NULL AUTO_INCREMENT,
    AchievementId SMALLINT NOT NULL,
    EventId       SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (AchievementId) REFERENCES Achievement (Id),
    FOREIGN KEY (EventId) REFERENCES Event (Id)
);
""")

cursor.execute("""
CREATE TABLE PlayerXAchievement
(
    Id            SMALLINT    NOT NULL AUTO_INCREMENT,
    AchievementId SMALLINT    NOT NULL,
    PlayerId      SMALLINT    NOT NULL,
    Date          VARCHAR(19) NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (AchievementId) REFERENCES Achievement (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);
""")

cursor.execute("""
CREATE TABLE Player
(
    Id             SMALLINT    NOT NULL AUTO_INCREMENT,
    Name           VARCHAR(20) NOT NULL,
    HP             SMALLINT    NOT NULL,
    RaceId         SMALLINT    NOT NULL,
    SkillTreeId    SMALLINT    NOT NULL,
    ClassId        SMALLINT    NOT NULL,
    Coins          SMALLINT,
    CurrentQuestId SMALLINT    NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (RaceId) REFERENCES Race (Id),
    FOREIGN KEY (SkillTreeId) REFERENCES SkillTree (Id)
);
""")

cursor.execute("""
CREATE TABLE Race
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE SkillTree
(
    Id        SMALLINT NOT NULL AUTO_INCREMENT,
    AbilityId SMALLINT,
    TalentId  SMALLINT,
    PRIMARY KEY (Id),
    FOREIGN KEY (AbilityId) REFERENCES Ability (Id),
    FOREIGN KEY (TalentId) REFERENCES Talent (Id)
);
""")

cursor.execute("""
CREATE TABLE Ability
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(30) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Talent
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(30) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE TradeOffer
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT,
    FromPlayerId SMALLINT NOT NULL,
    ToPlayerId   SMALLINT NOT NULL,
    ItemId       SMALLINT NOT NULL,
    Price        SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (FromPlayerId) REFERENCES Player (Id),
    FOREIGN KEY (ToPlayerId) REFERENCES Player (Id),
    FOREIGN KEY (ItemId) REFERENCES InventoryXItem (ItemID)
);
""")

cursor.execute("""
CREATE TABLE TeamXPlayerXRole
(
    Id         SMALLINT NOT NULL AUTO_INCREMENT,
    PlayerId   SMALLINT NOT NULL,
    TeamRoleId SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (TeamRoleId) REFERENCES TeamRole (Id)
);
""")

cursor.execute("""
CREATE TABLE TeamRole
(
    Id     SMALLINT    NOT NULL AUTO_INCREMENT,
    Name   VARCHAR(30) NOT NULL,
    TeamId SMALLINT    NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (TeamId) REFERENCES Team (Id)
);
""")

cursor.execute("""
CREATE TABLE Team
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(30) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Kingdom
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(30) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE PlayerCustomization
(
    Id               SMALLINT NOT NULL AUTO_INCREMENT,
    PlayerId         SMALLINT NOT NULL,
    OutfitItemId     SMALLINT NOT NULL,
    WeaponSkinItemId SMALLINT NOT NULL,
    EmoteItemId      SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);
""")

cursor.execute("""
CREATE TABLE Reward
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT,
    Name SMALLINT NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Quest
(
    Id               SMALLINT    NOT NULL AUTO_INCREMENT,
    Name             VARCHAR(30) NOT NULL,
    RewardId         SMALLINT    NOT NULL,
    ObjectiveId      SMALLINT    NOT NULL,
    CompletedAsATeam BOOLEAN     NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (RewardId) REFERENCES Reward (Id),
    FOREIGN KEY (ObjectiveId) REFERENCES Objective (Id)
);
""")

cursor.execute("""
CREATE TABLE ObjectiveXQuest
(
    Id           SMALLINT NOT NULL AUTO_INCREMENT,
    ObjectiveId  SMALLINT NOT NULL,
    QuestId      SMALLINT NOT NULL,
    IsCurrent    BOOLEAN  NOT NULL,
    PlayerId     SMALLINT NOT NULL,
    DifficultyId SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (ObjectiveId) REFERENCES Objective (Id),
    FOREIGN KEY (QuestId) REFERENCES Quest (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (DifficultyId) REFERENCES Difficulty (Id)
);
""")

cursor.execute("""
CREATE TABLE Objective
(
    Id      SMALLINT     NOT NULL AUTO_INCREMENT,
    Name    VARCHAR(100) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Difficulty
(
    Id   SMALLINT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(20),
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE PlayerAnalytics
(
    Id                 SMALLINT NOT NULL AUTO_INCREMENT,
    PlayerId           SMALLINT NOT NULL,
    HoursPlayed        DOUBLE   NOT NULL,
    NumberOfDeaths     SMALLINT NOT NULL,
    ItemsCrafted       SMALLINT NOT NULL,
    NPCEncountered     SMALLINT NOT NULL,
    PlayersEncountered SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id)
);
""")

cursor.execute("""
CREATE TABLE GuildCategory
(
    Id   SMALLINT    NOT NULL AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Id)
);
""")

cursor.execute("""
CREATE TABLE Guild
(
    Id              SMALLINT    NOT NULL AUTO_INCREMENT,
    Name            VARCHAR(50) NOT NULL,
    GuildCategoryId SMALLINT    NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (GuildCategoryId) REFERENCES GuildCategory (Id)
);
""")

cursor.execute("""
CREATE TABLE GuildXPlayer
(
    Id       SMALLINT NOT NULL AUTO_INCREMENT,
    PlayerId SMALLINT NOT NULL,
    GuildId  SMALLINT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (PlayerId) REFERENCES Player (Id),
    FOREIGN KEY (GuildId) REFERENCES Guild (Id)
);
""")
