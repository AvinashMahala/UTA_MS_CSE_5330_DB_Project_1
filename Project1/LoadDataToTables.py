
import oracledb
import csv
import datetime
from datetime import datetime as dt


noOfRowsCutOff=5000

def insertDataIntoGamesTable(conn):
    # Open the CSV file and create a CSV reader object
    with open('.\MySampleData\games.csv', 'r') as csv_file:     
        reader = csv.reader(csv_file, delimiter=',')
        print(f"Inserting Rows......")
        # Skip header row
        next(reader)
        rowNum=0
        # Loop through each row in the CSV file

        for row in reader:
            # Extract values from the row
            gameId = row[0]
            season = row[1]
            week = row[2]
            gameDate = row[3]
            gameTimeEastern = row[4]
            homeTeamAbbr = row[5]
            visitorTeamAbbr = row[6]
            
       
           
            cur = conn.cursor()
                
            cur.execute("INSERT INTO Games(gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) \
                            VALUES (:1, :2, :3,TO_DATE(:4, 'MM/DD/YYYY'), TO_TIMESTAMP(:5 || ' ' || :6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)",
                        (gameId, season, week, gameDate, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr))

            # Commit the transaction
            conn.commit()
            rowNum+=1
            if(rowNum>noOfRowsCutOff):
                break

        # Close the cursor
        cur.close()


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

def insertDataIntoPlaysTable(conn):
    # Open CSV file and create a CSV reader object
    rowNum=0
    with open('.\MySampleData\plays.csv') as csv_file:
        reader = csv.DictReader(csv_file)
    
        
        for row in reader:            
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
    
            cur = conn.cursor()
            
            # Insert row into the Plays table
            cur.execute("INSERT INTO Plays(gameId, playId, playDescription, \
            quarter, down, yardsToGo, possessionTeam, defensiveTeam, \
            yardlineSide, yardlineNumber, gameClock, \
            preSnapHomeScore, preSnapVisitorScore, passResult, \
            penaltyYards, prePenaltyPlayResult, playResult, foulName1, foulNFLId1, \
            foulName2, foulNFLId2, foulName3, foulNFLId3, absoluteYardlineNumber, \
            offenseFormation, personnelO, defendersInTheBox, personnelD, dropBackType, \
            pff_playAction, pff_passCoverage, pff_passCoverageType) \
            VALUES (:gameId, :playId, :playDescription, :quarter, :down, :yardsToGo, \
            :possessionTeam, :defensiveTeam, :yardlineSide, :yardlineNumber, \
            :gameClock, :preSnapHomeScore, :preSnapVisitorScore, :passResult, :penaltyYards, \
            :prePenaltyPlayResult, :playResult, :foulName1, :foulNFLId1, :foulName2, \
            :foulNFLId2, :foulName3, :foulNFLId3, :absoluteYardlineNumber, :offenseFormation,\
            :personnelO, :defendersInTheBox, :personnelD, :dropbackType, :pff_playAction, \
            :pff_passCoverage, :pff_passCoverageType)",
            {'gameId': gameId, 'playId': playId, 'playDescription': playDescription, \
             'quarter': quarter, 'down': down, 'yardsToGo': yardsToGo, \
            'possessionTeam': possessionTeam, 'defensiveTeam': defensiveTeam, \
            'yardlineSide': yardlineSide, 'yardlineNumber': yardlineNumber, \
            'gameClock': gameClock, 'preSnapHomeScore': preSnapHomeScore, \
            'preSnapVisitorScore': preSnapVisitorScore, 'passResult': passResult, \
            'penaltyYards': penaltyYards, 'prePenaltyPlayResult': prePenaltyPlayResult, \
            'playResult': playResult, 'foulName1': foulName1, 'foulNFLId1': foulNFLId1, \
            'foulName2': foulName2, 'foulNFLId2': foulNFLId2, 'foulName3': foulName3, \
            'foulNFLId3': foulNFLId3, 'absoluteYardlineNumber': absoluteYardlineNumber, \
            'offenseFormation': offenseFormation, 'personnelO': personnelO, \
            'defendersInTheBox': defendersInTheBox, 'personnelD': personnelD, \
            'dropbackType': dropbackType, 'pff_playAction': pff_playAction, \
            'pff_passCoverage': pff_passCoverage, 'pff_passCoverageType': pff_passCoverageType})
    
            # Commit the transaction
            conn.commit()
            rowNum+=1
            if(rowNum>noOfRowsCutOff):
                break
        print(f"Inserted {rowNum} rows.")
        # Close the cursor
        cur.close()
        print("---------Insert Complete-------------------")
        
        
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
        
        



def insertDataIntoPlayersTable(conn):
    rowNum=0
    
    with open('.\MySampleData\players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        cur = conn.cursor()
        print(f"Inserting Rows......")
        # Loop through each row in the CSV file
        for row in reader:
            # Extract the data from the row
            nflId = row['nflId']
            height = row['height']
            weight = row['weight']
            birthDate = formatDateField(row['birthDate'])
            collegeName = row['collegeName']
            officialPosition = row['officialPosition']
            displayName = row['displayName']
    
            # Define the SQL statement to insert the data into the table
            sql = "INSERT INTO Players (nflId, height, weight, birthDate, collegeName, officialPosition, displayName) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7)"
    
            # Define the values to insert into the table
            values = (nflId, height, weight, birthDate, collegeName, officialPosition, displayName)
    
            # Execute the SQL statement with the values
            cur.execute(sql, values)
            rowNum+=1
    
            # Commit the transaction
            conn.commit()
            if(rowNum>noOfRowsCutOff):
                break
        print(f"Inserted {rowNum} rows.")
        # Close the cursor
        cur.close()
        print("---------Insert Complete-------------------")
    
    


def insertDataIntoScoutingTable(conn):
    rowNum=0
    # Open the CSV file and read its contents
    cur = conn.cursor()
    with open('.\MySampleData\pffScoutingData.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    
        # Loop through each row in the CSV file
        for row in reader:
            # Extract the data from the row
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
            
            # Define the SQL statement to insert the data into the table
            sql = "INSERT INTO Scouting (gameId, playId, nflId, pff_role, pff_positionLinedUp, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_hurryAllowed, pff_sackAllowed, pff_nflIdBlockedPlayer, pff_blockType, pff_backFieldBlock) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15)"
    
            # Define the values to insert into the table
            values = (gameId, playId, nflId, pff_role, pff_positionLinedUp, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_hurryAllowed, pff_sackAllowed, pff_nflIdBlockedPlayer, pff_blockType, pff_backFieldBlock)
    
            # Execute the SQL statement with the values
            cur.execute(sql, values)

            # Commit the transaction
            conn.commit()
            rowNum+=1
            if(rowNum>noOfRowsCutOff):
                break
        print(f"Inserted {rowNum} rows.")
        # Close the cursor
        cur.close()
        print("---------Insert Complete-------------------")
    
    
def assignFloatNoneOrValue(val):
    if(val=='NA'):
        return None
    else:
        return float(val)

def insertDataIntoTrackingSampleWeekTable(conn):
    # create a cursor object
    cur = conn.cursor()
    rowNum=0
    # open the CSV file and read data
    with open('.\MySampleData\week1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # define variables for each column in the CSV file
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
    
            # define the SQL query to insert the row
            sql = "INSERT INTO Tracking_Sample_Week(gameId, playId, nflId, frameId, time, jerseyNumber, club, playDirection, x, y, s, a, dis, o, dir, event) VALUES (:gameId, :playId, :nflId, :frameId, TO_TIMESTAMP(:time, 'YYYY-MM-DD\"T\"HH24:MI:SS.FF'), :jerseyNumber, :club, :playDirection, :x, :y, :s, :a, :dis, :o, :dir, :event)"
    
            # define the values to insert
            values = {
                'gameId': gameId,
                'playId': playId,
                'nflId': nflId,
                'frameId': frameId,
                'time': time,
                'jerseyNumber': jerseyNumber,
                'club': club,
                'playDirection': playDirection,
                'x': x,
                'y': y,
                's': s,
                'a': a,
                'dis': dis,
                'o': o,
                'dir': dir,
                'event': event
            }
            cur.execute(sql, values)
            
            # Commit the transaction
            conn.commit()
            rowNum+=1
            if(rowNum>900):
                break
        print(f"Inserted {rowNum} rows.")
        # Close the cursor
        cur.close()
        print("---------Insert Complete-------------------")



if(__name__=="__main__"):
    conn = oracledb.connect(user="axm9433", password="Rameswar1996",
                            host="az6F72ldbp1.az.uta.edu", port=1523, service_name="pcse1p.data.uta.edu")
    if(conn):
        print(conn)
        print("Successfully connected to Oracle Database")
        print(conn.version)
        start_time = dt.now()
        #Uncomment the below functions one by one to import data.
        
        #insertDataIntoGamesTable(conn)
        #insertDataIntoPlaysTable(conn)
        #insertDataIntoPlayersTable(conn)
        #insertDataIntoScoutingTable(conn)
        insertDataIntoTrackingSampleWeekTable(conn)
        end_time = dt.now()
        print("Elapsed time: {}".format(end_time - start_time))
    else:
        print("Connection Failed!!!!")
        
        
    conn.close()
    


