'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import cx_Oracle
import csv
import datetime
from datetime import datetime as dt
from datetime import time


noOfRowsCutOff=5000

def assignFloatNoneOrValue(val):
    if(val=='NA'):
        return None
    else:
        return float(val)
    
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
file_path = ".\MySampleData\week1.csv"
table_name = "Tracking_Sample_Week"

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
        nflId = assignIntNoneOrValue(row['nflId'])
        frameId = row['frameId']
        time = row['time']
        jerseyNumber =assignIntNoneOrValue(row['jerseyNumber'])
        club = row['team']
        playDirection = row['playDirection']
        x = assignFloatNoneOrValue(row['x'])
        y = assignFloatNoneOrValue(row['y'])
        s = assignFloatNoneOrValue(row['s'])
        a = assignFloatNoneOrValue(row['a'])
        dis = assignFloatNoneOrValue(row['dis'])
        o = assignFloatNoneOrValue(row['o'])
        dir = assignFloatNoneOrValue(row['dir'])
        event = assignStringNoneOrValue(row['event'])
        
        #print(list(row.values()))
        if(nflId!=None):
            rows.append(list([gameId,playId,nflId,frameId,time,jerseyNumber,club,playDirection,x,y,s,a,dis,o,dir,event]))
        
        
        
        #print(list([gameId,season,week,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        # If the row buffer is full, insert the rows into the table and reset the row buffer
        if len(rows) == batch_size and (batch_count * batch_size)<noOfRowsCutOff:
            print("1")
            #print(rows)
            with connection.cursor() as cursor:
                cursor.executemany("INSERT INTO Tracking_Sample_Week(gameId, playId, nflId, frameId, time, jerseyNumber, club, playDirection, x, y, s, a, dis, o, dir, event) VALUES (:gameId, :playId, :nflId, :frameId, TO_TIMESTAMP(:time, 'YYYY-MM-DD\"T\"HH24:MI:SS.FF'), :jerseyNumber, :club, :playDirection, :x, :y, :s, :a, :dis, :o, :dir, :event)",
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
           cursor.executemany("INSERT INTO Tracking_Sample_Week(gameId, playId, nflId, frameId, time, jerseyNumber, club, playDirection, x, y, s, a, dis, o, dir, event) VALUES (:gameId, :playId, :nflId, :frameId, TO_TIMESTAMP(:time, 'YYYY-MM-DD\"T\"HH24:MI:SS.FF'), :jerseyNumber, :club, :playDirection, :x, :y, :s, :a, :dis, :o, :dir, :event)",
               rows)

        # Print a final progress message
        print(f"Inserted {len(rows)} rows")
    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
