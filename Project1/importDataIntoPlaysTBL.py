'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import cx_Oracle
import csv
import datetime
from datetime import datetime as dt
from datetime import time

noOfRowsCutOff=5000

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
    
    
# Connection details
username = "axm9433"
password = "Rameswar1996"
hostname = "az6F72ldbp1.az.uta.edu"
port = "1523"
service_name = "pcse1p.data.uta.edu"

# File path and name
file_path = ".\MySampleData\plays.csv"
table_name = "Plays"

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
        
        gameId = int(row['gameId'])
        playId = int(row['playId'])
        playDescription = row['playDescription']
        quarter = int(row['quarter'])
        down = int(row['down'])
        yardsToGo = int(row['yardsToGo'])
        possessionTeam = row['possessionTeam']
        defensiveTeam = row['defensiveTeam']
        yardlineSide = row['yardlineSide']
        yardlineNumber = int(row['yardlineNumber'])
        gameClock = row['gameClock']
        preSnapHomeScore = int(row['preSnapHomeScore'])
        preSnapVisitorScore = int(row['preSnapVisitorScore'])
        passResult = row['passResult']
        penaltyYards = assignIntNoneOrValue(row['penaltyYards'])
        prePenaltyPlayResult = assignIntNoneOrValue(row['prePenaltyPlayResult'])
        playResult = assignIntNoneOrValue(row['playResult'])
        
        foulName1 = assignStringNoneOrValue(row['foulName1'])
        
        foulNFLId1 = assignIntNoneOrValue(row['foulNFLId1'])
        foulName2 = assignStringNoneOrValue(row['foulName2'])
        foulNFLId2 = assignIntNoneOrValue(row['foulNFLId2'])
        foulName3 = assignStringNoneOrValue(row['foulName3'])
        foulNFLId3 = assignIntNoneOrValue(row['foulNFLId3'])
        absoluteYardlineNumber = assignIntNoneOrValue(row['absoluteYardlineNumber'])
        offenseFormation = row['offenseFormation']
        personnelO = row['personnelO']
        defendersInTheBox = assignIntNoneOrValue(row['defendersInBox'])
        personnelD = row['personnelD']
        dropbackType = row['dropBackType']
        pff_playAction = row['pff_playAction']
        pff_passCoverage = row['pff_passCoverage']
        pff_passCoverageType = row['pff_passCoverageType']
        
        
        
        #print(list(row.values()))
        rows.append(list([gameId,playId,playDescription,quarter,down,yardsToGo,possessionTeam,defensiveTeam,yardlineSide,yardlineNumber,gameClock,preSnapHomeScore,preSnapVisitorScore,passResult,penaltyYards,prePenaltyPlayResult,playResult,foulName1,foulNFLId1,foulName2,foulNFLId2,foulName3,foulNFLId3,absoluteYardlineNumber,offenseFormation,personnelO,defendersInTheBox,personnelD,dropbackType,pff_playAction,pff_passCoverage,pff_passCoverageType]))
        
        #print(list([gameId,season,week,gameDate,gameTimeEastern,homeTeamAbbr,visitorTeamAbbr]))
        # If the row buffer is full, insert the rows into the table and reset the row buffer
        if len(rows) == batch_size and (batch_count * batch_size)<noOfRowsCutOff:
            print("1")
            with connection.cursor() as cursor:
                cursor.executemany("INSERT INTO Plays(gameId, playId, playDescription, \
                quarter, down, yardsToGo, possessionTeam, defensiveTeam, \
                yardlineSide, yardlineNumber, gameClock, \
                preSnapHomeScore, preSnapVisitorScore, passResult, \
                penaltyYards, prePenaltyPlayResult, playResult, foulName1, foulNFLId1, \
                foulName2, foulNFLId2, foulName3, foulNFLId3, absoluteYardlineNumber, \
                offenseFormation, personnelO, defendersInTheBox, personnelD, dropBackType, \
                pff_playAction, pff_passCoverage, pff_passCoverageType) \
                VALUES (:1, :2, :3, :4, :5, :6, \
                :7, :8, :9, :10, \
                :11, :12, :13, :14, :15, \
                :16, :17, :18, :19, :20, \
                :21, :22, :23, :24, :25,\
                :26, :27, :28, :29, :30, \
                :31, :32)",
                    rows)

            # Increment the batch counter and reset the row buffer
            batch_count += 1
            rows = []

            # Print a progress message
            print(f"Inserted {batch_count * batch_size} rows")

    # If there are any rows left in the buffer, insert them into the table
    if(((batch_count * batch_size)<noOfRowsCutOff)):
        with connection.cursor() as cursor:
            cursor.executemany("INSERT INTO Plays(gameId, playId, playDescription, \
            quarter, down, yardsToGo, possessionTeam, defensiveTeam, \
            yardlineSide, yardlineNumber, gameClock, \
            preSnapHomeScore, preSnapVisitorScore, passResult, \
            penaltyYards, prePenaltyPlayResult, playResult, foulName1, foulNFLId1, \
            foulName2, foulNFLId2, foulName3, foulNFLId3, absoluteYardlineNumber, \
            offenseFormation, personnelO, defendersInTheBox, personnelD, dropBackType, \
            pff_playAction, pff_passCoverage, pff_passCoverageType) \
            VALUES (:1, :2, :3, :4, :5, :6, \
            :7, :8, :9, :10, \
            :11, :12, :13, :14, :15, \
            :16, :17, :18, :19, :20, \
            :21, :22, :23, :24, :25,\
            :26, :27, :28, :29, :30, \
            :31, :32)",
                rows)

        # Print a final progress message
        print(f"Inserted {len(rows)} rows")

    # Commit the changes to the database
    connection.commit()

# Close the database connection
connection.close()
