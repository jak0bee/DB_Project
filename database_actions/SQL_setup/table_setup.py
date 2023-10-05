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

CREATE TABLE Kingdom
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

-- Tables with foreign keys (depends on previous tables)
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
    Coins       SMALLINT             DEFAULT 0,
    FOREIGN KEY (RaceId) REFERENCES Race (Id),
    FOREIGN KEY (SkillTreeId) REFERENCES SkillTree (Id)
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
