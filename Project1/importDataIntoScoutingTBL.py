'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import cx_Oracle
import csv
import datetime
from datetime import datetime as dt
from datetime import time


noOfRowsCutOff=15000


def assignIntNoneOrValue(val):
    if(val=='NA'):
        return None
    else:
        return int(val)
    
def assignStringNoneOrValue(val):
    if(val=='NA' or 'None'):
        return None
    else:
        return val

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
file_path = ".\MySampleData\pffScoutingData.csv"
table_name = "Scouting"

# Batch size
batch_size = 1000

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
        
        gameId = row['gameId']
        playId = row['playId']
        nflId = row['nflId']
        pff_role = row['pff_role']
        pff_positionLinedUp = row['pff_positionLinedUp']
        pff_hit = assignStringNoneOrValue(row['pff_hit'])
        pff_hurry = assignStringNoneOrValue(row['pff_hurry'])
        pff_sack = assignStringNoneOrValue(row['pff_sack'])
        pff_beatenByDefender = assignStringNoneOrValue(row['pff_beatenByDefender'])
        pff_hitAllowed = assignStringNoneOrValue(row['pff_hitAllowed'])
        pff_hurryAllowed = assignStringNoneOrValue(row['pff_hurryAllowed'])
        pff_sackAllowed = assignStringNoneOrValue(row['pff_sackAllowed'])
        pff_nflIdBlockedPlayer = assignIntNoneOrValue(row['pff_nflIdBlockedPlayer'])
        pff_blockType = assignStringNoneOrValue(row['pff_blockType'])
        pff_backFieldBlock = assignStringNoneOrValue(row['pff_backFieldBlock'])
        
        #print(list(row.values()))
        rows.append(list([gameId, playId, nflId, pff_role, pff_positionLinedUp, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_hurryAllowed, pff_sackAllowed, pff_nflIdBlockedPlayer, pff_blockType, pff_backFieldBlock]))
        
        
        
        #print(list([gameId,season,week,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        # If the row buffer is full, insert the rows into the table and reset the row buffer
        if len(rows) == batch_size and (batch_count * batch_size)<noOfRowsCutOff:
            print("1")
            with connection.cursor() as cursor:
                cursor.executemany("INSERT INTO Scouting (gameId, playId, nflId, pff_role, pff_positionLinedUp, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_hurryAllowed, pff_sackAllowed, pff_nflIdBlockedPlayer, pff_blockType, pff_backFieldBlock) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15)",
                    rows)

            # Increment the batch counter and reset the row buffer
            batch_count += 1
            rows = []

            # Print a progress message
            print(f"Inserted {batch_count * batch_size} rows")

    # If there are any rows left in the buffer, insert them into the table
    if(((batch_count * batch_size)<noOfRowsCutOff)):
        print("0")
        with connection.cursor() as cursor:
           cursor.executemany("INSERT INTO Scouting (gameId, playId, nflId, pff_role, pff_positionLinedUp, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_hurryAllowed, pff_sackAllowed, pff_nflIdBlockedPlayer, pff_blockType, pff_backFieldBlock) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15)",
               rows)

        # Print a final progress message
        print(f"Inserted {len(rows)} rows")
        
    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
