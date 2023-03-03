CREATE TABLE Games(
    gameId NUMBER(10),
    season NUMBER(4),
    week NUMBER(2),
    gameDate DATE,
    gameTimeEastern TIMESTAMP,
    homeTeamAbbr VARCHAR2(3),
    visitorTeamAbbr VARCHAR2(3),
    CONSTRAINT pk_Games_gameId PRIMARY KEY (gameId)
);
--truncate table games;
select * from games;

--------------------------------------------------------------------------------
/*
TABLE NAME-Plays

ALTER TABLE Plays DROP CONSTRAINT pk_Plays_gameId_playId;
ALTER TABLE Plays DROP CONSTRAINT fk_Plays_Game;
DROP Table Plays;

*/


--------------------------------------------------------------------------------
CREATE TABLE Plays (
    gameId NUMBER(10),
    playId NUMBER(10),
    playDescription VARCHAR2(4000),
    quarter NUMBER(2),
    down NUMBER(1),
    yardsToGo NUMBER(2),
    possessionTeam VARCHAR2(3),
    defensiveTeam VARCHAR2(3),
    yardlineSide VARCHAR2(3),
    yardlineNumber NUMBER(3),
    gameClock VARCHAR2(5),
    preSnapHomeScore NUMBER(3),
    preSnapVisitorScore NUMBER(3),
    passResult VARCHAR2(2),
    penaltyYards NUMBER(2),
    prePenaltyPlayResult NUMBER(3),
    playResult NUMBER(3),
    foulName1 VARCHAR2(100),
    foulName2 VARCHAR2(100),
    foulName3 VARCHAR2(100),
    foulNFLId1 NUMBER(10),
    foulNFLId2 NUMBER(10),
    foulNFLId3 NUMBER(10),
    absoluteYardlineNumber NUMBER(3),
    offenseFormation VARCHAR2(100),
    personnelO VARCHAR2(100),
    defendersInTheBox NUMBER(2),
    personnelD VARCHAR2(100),
    dropbackType VARCHAR2(100),
    pff_playAction CHAR(1),
    pff_passCoverage VARCHAR2(100),
    pff_passCoverageType VARCHAR2(10),
    CONSTRAINT pk_Plays_gameId_playId PRIMARY KEY (gameId, playId),
    CONSTRAINT fk_Plays_Game FOREIGN KEY (gameId) REFERENCES Games(gameId) ON DELETE CASCADE
);
--------------------------------------------------------------------------------


--truncate table plays;
select * from plays;
select count(*) from plays;






