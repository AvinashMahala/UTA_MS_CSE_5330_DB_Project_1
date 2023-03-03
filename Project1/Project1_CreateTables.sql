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
insert into games values(123,1,2,TO_DATE('09/09/2021','MM/DD/YYYY'),
TO_TIMESTAMP ('09/09/2021 14:10:10', 'MM/DD/YYYY HH24:MI:SS'),'AA','BB')





--truncate table games;
select * from games;


select sysdate from dual
select TO_DATE('09/09/2021','DD/MM/YYYY') from dual;



SELECT TO_TIMESTAMP ('14:10:10', 'HH24:MI:SS')
   FROM DUAL;


SELECT TOTIME(
    '09/09/2021',
    'MM/DD/YYYY',
     'NLS_DATE_LANGUAGE = American')
     FROM DUAL;

TO_DATE('
---------
15-JAN-89



Value
---------
01-JAN-16
