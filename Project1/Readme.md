CSE5330                           Spring 2023
Project 1
In this project, you will get started on how to use a relational DBMS. You can either use the 
ORACLE RDBMS, or the MySQL system in Omega. You will use the interactive SQLPLUS 
facility, and the SQL programming facility, by creating tables, populating them with data, 
and querying and updating the tables. You will be using the NFL Big Data Bowl data from 
Kaggle (NFL Big Data Bowl 2023 | Kaggle ). You should do the following:
1. Create the following tables for the NFL 2023 database whose schema descriptions are in website 
(NFL Big Data Bowl 2023 | Kaggle) . The relations would be Games, Plays, Players, Scouting, 
Tracking_Sample_Week. Derive your keys and other constraints from the dataset description 
page mentioned in the above site.
2. Write your CREATE TABLE statements (DDL) in a text file, and execute the commands 
from the file through SQLPLUS. You should capture the execution in a spool file that will 
be turned in. Specify appropriate key and referential integrity constraints. The data 
types for each attribute are given after the schema diagram.
3. Write one or more database programs to load the records that will be provided to you 
into each of the tables that you created.  You can use any programming or scripting 
language you are familiar with (JAVA with JDBC, Python, etc.).
4. Write down the queries for the English queries that will be supplied later. Execute each 
query and display its results. Capture your commands in spool files for turning in.
5. Execute 3 more Insert commands that attempt to insert 3 more records, such that the 
records violate the integrity constraints. Make each of the 3 records violate a different 
type of integrity constraint. Capture your commands in spool files for turning in.
6. Execute a SQL command to Delete a record that violates a referential integrity 
constraint. Capture your command in a spool file for turning in.
7. Repeat 5, but Insert three new records that do not violate any integrity constraints. 
Capture your commands in spool files for turning in.
You should turn in to the GTA one or more Spool files as part of this assignment, including 
creating the tables and the query results. You should also turn in the source code for the 
programming part of the assignment for loading the data. 
Document your output when needed by writing down an explanation for each step (by 
editing the spool file); for example, explain the integrity constraints violated in item 5.
Make a zip file with all the files together and submit it through blackboard.
Important Notes:
(1) This project can be done individually, or in a two-person group. If two persons do the 
project, they will receive the same grade.
(2) Copying from other students or groups is not permitted and will result in a grade of 
zero for the entire project.
Due Dates: There are two due dates: 
1. March 5, 2023 before midnight is the due date for creating the tables and loading 
the data. The table schema and data can be found at Kaggle website 
(https://www.kaggle.com/competitions/nfl-big-data-bowl-2023/data).
2. March 12, 2023 before midnight is for the rest of the project (queries and updates). 
The required queries and updates will be supplied later on.
Hope the practice that you have done for tests will help you in this project.
Submit your assignment in Canvas any time before midnight of the due date. You should 
follow the instructions on how to turn in your project from TA. If you are doing the projects 
in a team of two, only one team member will submit the projects. Clearly specify your 
name, team member's name in the documentation of this project.

Late policy: -5% out of 100 for each day late.
