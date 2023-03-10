'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import cx_Oracle
import csv
import datetime
from datetime import datetime as dt
from datetime import time

noOfRowsCutOff=5000

def validate(date_text):
        try:
            datetime.date.fromisoformat(date_text)
            return True
        except ValueError:
            return False

def formatDateField(dtField):
    if(dtField=="NA"):
        return None
    else:
        if(validate(dtField)):
            return dtField
        else:
            split=dtField.split("/")
            dt=split[2]+'-'+split[0]+'-'+split[1]
            #print(dt)
            return dt
        
        
        
# Connection details
username = "axm9433"
password = "Rameswar1996"
hostname = "az6F72ldbp1.az.uta.edu"
port = "1523"
service_name = "pcse1p.data.uta.edu"

# File path and name
file_path = ".\MySampleData\players.csv"
table_name = "Players"

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
        
        nflId = row['nflId']
        height = row['height']
        weight = row['weight']
        birthDate = formatDateField(row['birthDate'])
        collegeName = row['collegeName']
        officialPosition = row['officialPosition']
        displayName = row['displayName']
        
        #print(list(row.values()))
        rows.append(list([nflId,height,weight,birthDate,collegeName,officialPosition,displayName]))
        
        
        
        #print(list([gameId,season,week,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        # If the row buffer is full, insert the rows into the table and reset the row buffer
        if len(rows) == batch_size and (batch_count * batch_size)<noOfRowsCutOff:
            print("1")
            with connection.cursor() as cursor:
                cursor.executemany("INSERT INTO Players (nflId, height, weight, birthDate, collegeName, officialPosition, displayName) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7)",
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
            cursor.executemany("INSERT INTO Players (nflId, height, weight, birthDate, collegeName, officialPosition, displayName) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7)",
                rows)

        # Print a final progress message
        print(f"Inserted {len(rows)} rows")

    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
