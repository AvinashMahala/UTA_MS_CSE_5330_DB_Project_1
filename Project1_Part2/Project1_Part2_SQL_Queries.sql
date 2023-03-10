set heading on
set linesize 1500
set colsep '|'
set numformat 99999999999999999999
set pagesize 25000
set echo on;
set serveroutput on;
Spool avinash_ameet_Proj_1_Part_2_spool_logs.txt append;
/*
Name - Avinash Mahala(1002079433) and Amit Munna Gupta(1002079433)
Project1_Part_2
*/

/*Games,Plays,Players,Scouting,Tracking_Sample_Week*/
Select Count(*) from Games;--122
Select Count(*) from Plays;--5001
Select Count(*) From Players;--1679
Select Count(*) from Scouting;--5001
Select Count(*) from Tracking_Sample_Week;--901

Spool avinash_ameet_Proj_1_Part_2_spool_logs.txt append;
-------------------------Start of Question 5----------------------------------------
/*
Q5)Execute 3 more Insert commands that attempt to insert 3 more records, such that the 
records violate the integrity constraints. Make each of the 3 records violate a different 
type of integrity constraint. Capture your commands in spool files for turning in.
*/

/*
(a)Integrity Violation 1(Insert a duplicate primary key value):
---------------------------------------------------
Select * From Games where GameID = '2021090900';

Here The Games Table has already a record with PrimaryKey(GameID) '2021090900'.
But I am trying to reinsert it using the below Command.
*/
Insert Into Games values(2021090900,2021,1,'09-09-21','09-09-21 8:20:00.000000000 PM','TB','DAL');

/*
----------------------------------------------------
While Running the above Query It shows the below error in ORACLE SQL DB:
----------------------------------------------------
Error starting at line : 14 in command -
Insert Into Games values(2021090900,2021,1,'09-09-21','09-09-21 8:20:00.000000000 PM','TB','DAL')
Error report -
ORA-00001: unique constraint (AXM9433.PK_GAMES_GAMEID) violated
----------------------------------------------------
*/
--------------------------------------------------------------------------------

/*
(b)Integrity Violation 2(Insert a foreign key value that does not exist in the parent table):

Here let 'GAMES' is Parent Table and 'PLAYS' is the Child Table.
Now We will try to insert a record in Child Table for which foreign does not exist
in the Parent Table 'GAMES'

Select * From Games where GameID = '2051090909';
Here When We run the above Command the query result is blank as the GameID 
'2051090909' is not present in the GAMES Table.

Now lets try to insert a record in Table 'PLAYS' using '2051090909'.
*/
Insert into AXM9433.PLAYS (GAMEID,PLAYID,PLAYDESCRIPTION,QUARTER,DOWN,YARDSTOGO,POSSESSIONTEAM,
DEFENSIVETEAM,YARDLINESIDE,YARDLINENUMBER,GAMECLOCK,PRESNAPHOMESCORE,
PRESNAPVISITORSCORE,PASSRESULT,PENALTYYARDS,PREPENALTYPLAYRESULT,PLAYRESULT,
FOULNAME1,FOULNAME2,FOULNAME3,FOULNFLID1,FOULNFLID2,FOULNFLID3,ABSOLUTEYARDLINENUMBER,
OFFENSEFORMATION,PERSONNELO,DEFENDERSINTHEBOX,PERSONNELD,DROPBACKTYPE,PFF_PLAYACTION,
PFF_PASSCOVERAGE,PFF_PASSCOVERAGETYPE) 
values 
(2051090909,2915,'Sample Description',3,3,10,'TB','DAL','TB',33,'09:00',21,19,'I',0,0,0,
null,null,null,52421,null,null,77,'SHOTGUN','1 RB, 1 TE, 3 WR',5,'3 DL, 3 LB, 5 DB',
'TRADITIONAL','0','Cover-2','Zone');
--------------------------------------------------------------------------------
/*
Now When I ran this above command I got the Error as below:
Error starting at line : 46 in command -

Error report -
ORA-02291: integrity constraint (AXM9433.FK_PLAYS_GAME) violated - parent key not found
*/

--------------------------------------------------------------------------------
/*

/*
(c)Integrity Violation 3(Violating UNIQUE Constraint):

In "Games" Table the Columns (HOMETEAMABBR,VISITORTEAMABBR) together consists a Unique Key.
If any duplicate combination is tried to insert then an error will occur.

For Example the combination ('TB','DAL') is already present for a record having GameID
'2021090900'. Now we will try to insert another record using this combination for
new GameID.

The Command is as follows:-
*/
Insert Into Games values(2051090909,2021,1,'09-09-21','09-09-21 8:20:00.000000000 PM','TB','DAL');
/*
Here although the Primary Key is different(2051090909), but the combination ('TB','DAL') has
already been used once in the Games Table. Hence if we try to insert again it will 
result in error as below:-

Error report -
ORA-00001: unique constraint (AXM9433.UNIQUE_HTA_VTA_COMBINATION) violated
*/
-------------------------End of Question 5----------------------------------------


Spool avinash_ameet_Proj_1_Part_2_spool_logs.txt append;
-------------------------Start of Question 6----------------------------------------
/*
Q6)Execute a SQL command to Delete a record that violates a referential integrity 
constraint. Capture your command in a spool file for turning in.
*/
/*
SELECT gameId, COUNT(*) as count
FROM Plays
GROUP BY gameId
HAVING COUNT(*) > 1
AND COUNT(*) NOT IN (SELECT COUNT(*) FROM Games WHERE gameId = Plays.gameId);
*/
/*
Let Parent table be 'Games' and Child Table be 'Plays'.
Now we will try to delete a record from parent table having gameid '2021091211'.
The command is:-
*/
delete from games where gameid=2021091211;
/*
The above command will result in an error stating as below:-
Error report -
ORA-02292: integrity constraint (AXM9433.FK_PLAYS_GAME) violated - child record found
*/

-------------------------End of Question 6----------------------------------------


Spool avinash_ameet_Proj_1_Part_2_spool_logs.txt append;
-------------------------Start of Question 7----------------------------------------
/*
Q7)Repeat 5, but Insert three new records that do not violate any integrity constraints. 
Capture your commands in spool files for turning in.
*/
Insert Into Games values(2061090909,2021,1,'09-09-21','09-09-21 8:20:00.000000000 PM','TB','JAX');

Insert Into Games values(2051090909,2021,1,'09-09-21','09-09-21 8:20:00.000000000 PM','ATL','DEN');

Insert into PLAYS
values 
(2051090909,2915,'Sample Description',3,3,10,'TB','DAL','TB',33,'09:00',21,19,'I',0,0,0,
null,null,null,52421,null,null,77,'SHOTGUN','1 RB, 1 TE, 3 WR',5,'3 DL, 3 LB, 5 DB',
'TRADITIONAL','0','Cover-2','Zone');


select * from Games where GameId=2061090909;
select * from Games where GameId=2051090909;
select * from PLAYS where GameId=2051090909 and playid=2915;

-------------------------End of Question 7----------------------------------------






