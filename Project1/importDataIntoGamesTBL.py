'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import cx_Oracle
import csv
import datetime
from datetime import datetime as dt
from datetime import time

noOfRowsCutOff=5000

# Connection details
username = "axm9433"
password = "Rameswar1996"
hostname = "az6F72ldbp1.az.uta.edu"
port = "1523"
service_name = "pcse1p.data.uta.edu"

# File path and name
file_path = ".\MySampleData\games.csv"
table_name = "Games"

# Batch size
batch_size = 500

# Connect to the database
connection = cx_Oracle.connect(
    username, password, f"{hostname}:{port}/{service_name}")

# Open the CSV file
with open(file_path, newline="") as csvfile:
    # Read the file into a dictionary
    reader = csv.DictReader(csvfile)

    # Get the column names from the first row of the CSV file
    columns = list(reader.fieldnames)

    # Initialize the batch counter and row buffer
    batch_count = 0
    rows = []

    # Loop through each row in the CSV file
    for row in reader:
        # Add the row to the row buffer
        
        gameId = row["gameId"]
        season = row["season"]
        week = row["week"]
        
        gameDate = row["gameDate"]
        gameTimeEastern = row["gameTimeEastern"]
        
        homeTeamAbbr = row["homeTeamAbbr"]
        visitorTeamAbbr = row["visitorTeamAbbr"]
        
        
        #print("Inserting Rows......")
        
        print("gameId:", gameId)
        print("season:", season)
        print("week:", week)
        print("gameDate:", gameDate)
        print("gameTimeEastern:", gameTimeEastern)
        print("homeTeamAbbr:", homeTeamAbbr)
        print("visitorTeamAbbr:", visitorTeamAbbr)
        print("----------------------------------------------------------")
        
        #print(list(row.values()))
        rows.append(list([gameId,season,week,gameDate,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        
        #print(list([gameId,season,week,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        # If the row buffer is full, insert the rows into the table and reset the row buffer
        if len(rows) == batch_size and (batch_count * batch_size)<noOfRowsCutOff:
            print("1")
            with connection.cursor() as cursor:
                cursor.executemany("INSERT INTO Games(gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) \
                                    VALUES (:1, :2, :3,TO_DATE(:4, 'MM/DD/YYYY'), TO_TIMESTAMP(:5 || ' ' || :6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)",
                    rows)

            # Increment the batch counter and reset the row buffer
            batch_count += 1
            rows = []

            # Print a progress message
            print(f"Inserted {batch_count * batch_size} rows")

    # If there are any rows left in the buffer, insert them into the table
    if(((batch_count * batch_size)<noOfRowsCutOff)):
        print(rows[0])
        with connection.cursor() as cursor:
            cursor.executemany("INSERT INTO Games(gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) \
                                VALUES (:1, :2, :3,TO_DATE(:4, 'MM/DD/YYYY'), TO_TIMESTAMP(:5 || ' ' || :6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)",
                rows)

        # Print a final progress message
        print(f"Inserted {len(rows)} rows")

    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
