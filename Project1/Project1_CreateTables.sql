/*
Name - Avinash Mahala(1002079433) and Amit Munna Gupta(1002079433)
Project1_Part_1
*/


/*
Relations- Games, Plays, Players, Scouting, Tracking_Sample_Week
*/
----------------
-----Commands Only When Very Very Required Else Do Not Run
--PURGE RECYCLEBIN
----------------
--Spool avinash_spool.txt 
--Spool avinash_spool.txt 
--Spool off
--------------------------------------------------------------------------------
/*
Drop Queries:-
Drop Table Tracking_Sample_Week;
Drop Table Scouting;
Drop Table Players;
Drop Table Plays;
Drop Table Games;
*/

set heading on
set linesize 1500
set colsep '|'
set numformat 99999999999999999999
set pagesize 25000
set echo on;
set serveroutput on;
Spool avinash_ameet_spool_logs.txt append;
--------------------------------------------------------------------------------
/*
TABLE NAME-Games

--ALTER TABLE Games DROP CONSTRAINT pk_Games_gameId;
--DROP Table Games;
*/



CREATE TABLE Games(
    gameId NUMBER(10),
    season NUMBER(4),
    week NUMBER(2),
    gameDate DATE,
    gameTimeEastern TIMESTAMP,
    homeTeamAbbr VARCHAR2(3),
    visitorTeamAbbr VARCHAR2(3),
    CONSTRAINT pk_Games_gameId PRIMARY KEY (gameId),
    CONSTRAINT unique_hta_vta_combination UNIQUE (homeTeamAbbr,visitorTeamAbbr)
);

--delete from games;
--truncate table games
--select count(*) from games;
--select * from games;
--------------------------------------------------------------------------------
Spool avinash_ameet_spool_logs.txt append;
/*
TABLE NAME-Plays

--ALTER TABLE Plays DROP CONSTRAINT pk_Plays_gameId_playId;
--ALTER TABLE Plays DROP CONSTRAINT fk_Plays_Game;
--DROP Table Plays;
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
    CONSTRAINT fk_Plays_Game FOREIGN KEY (gameId) REFERENCES Games(gameId)
);
--------------------------------------------------------------------------------
--truncate table plays;
--select * from plays order by gameid,playid asc
--select count(*) from plays;
--------------------------------------------------------------------------------
Spool avinash_ameet_spool_logs.txt append;
/*
TABLE NAME-Players

--ALTER TABLE Players DROP CONSTRAINT pk_Players;
--DROP Table Players;
*/
--------------------------------------------------------------------------------
CREATE TABLE Players (
    nflId NUMBER(10),
    height VARCHAR2(10),
    weight NUMBER(3),
    birthDate DATE,
    collegeName VARCHAR2(100),
    officialPosition VARCHAR2(100),
    displayName VARCHAR2(100),
    CONSTRAINT pk_Players PRIMARY KEY (nflId)
);
--------------------------------------------------------------------------------
--delete from Players;
--truncate table Players;
--select * from Players;
--select count(*) from Players;

 commit;
--------------------------------------------------------------------------------
Spool avinash_ameet_spool_logs.txt append;
/*
TABLE NAME-Scouting

--ALTER TABLE Scouting DROP CONSTRAINT pk_Scouting;
--ALTER TABLE Scouting DROP CONSTRAINT fk_Scouting_Game;
--ALTER TABLE Scouting DROP CONSTRAINT fk_Scouting_Players;
--DROP Table Scouting;
*/
--------------------------------------------------------------------------------
CREATE TABLE Scouting (
    gameId NUMBER(10),
    playId NUMBER(10),
    nflId NUMBER(10),
    pff_role VARCHAR2(100),
    pff_positionLinedUp VARCHAR2(100),
    pff_hit CHAR(1),
    pff_hurry CHAR(1),
    pff_sack CHAR(1),
    pff_beatenByDefender CHAR(1),
    pff_hitAllowed CHAR(1),
    pff_hurryAllowed CHAR(1),
    pff_sackAllowed CHAR(1),
    pff_nflIdBlockedPlayer NUMBER(10),
    pff_blockType VARCHAR2(2),
    pff_backFieldBlock CHAR(1),
    CONSTRAINT pk_Scouting PRIMARY KEY (gameId, playId, nflId),
    CONSTRAINT fk_Scouting_Game FOREIGN KEY (gameId, playId) REFERENCES Plays(gameId, playId),
    CONSTRAINT fk_Scouting_Players FOREIGN KEY (nflId) REFERENCES Players(nflId)
);

--------------------------------------------------------------------------------
--PURGE RECYCLEBIN
--delete from Scouting;
--select * from Scouting;
--select count(*) from Scouting;
--------------------------------------------------------------------------------
Spool avinash_ameet_spool_logs.txt append;
/*
TABLE NAME-Tracking_Sample_Week

--ALTER TABLE Tracking_Sample_Week DROP CONSTRAINT pk_Tracking_Sample_Week;
--ALTER TABLE Tracking_Sample_Week DROP CONSTRAINT fk_Tracking_Sample_Week_Plays;
--ALTER TABLE Tracking_Sample_Week DROP CONSTRAINT fk_Tracking_Sample_Week_Players;
--DROP Table Tracking_Sample_Week;
*/
--------------------------------------------------------------------------------
CREATE TABLE Tracking_Sample_Week (
    gameId NUMBER(10),
    playId NUMBER(10),
    nflId NUMBER(10),
    frameId NUMBER(10),
    time TIMESTAMP,
    jerseyNumber NUMBER(3),
    club VARCHAR2(3),
    playDirection VARCHAR2(6),
    x NUMBER(10,2),
    y NUMBER(10,2),
    s NUMBER(10,2),
    a NUMBER(10,2),
    dis NUMBER(10,2),
    o NUMBER(10,2),
    dir NUMBER(10,2),
    event VARCHAR2(100),
    CONSTRAINT pk_Tracking_Sample_Week PRIMARY KEY (gameId, playId, nflId, frameId),
    CONSTRAINT fk_Tracking_Sample_Week_Plays FOREIGN KEY (gameId, playId) REFERENCES Plays(gameId, playId),
    CONSTRAINT fk_Tracking_Sample_Week_Players FOREIGN KEY (nflId) REFERENCES Players(nflId)
);

--------------------------------------------------------------------------------
--delete from Tracking_Sample_Week;
--select * from Tracking_Sample_Week;
--select count(*) from Tracking_Sample_Week;

spool off;