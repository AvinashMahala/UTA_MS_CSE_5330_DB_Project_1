'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import oracledb
import csv
from datetime import datetime

def insertDataIntoGamesTable(conn):
    # Open the CSV file and create a CSV reader object
    with open('.\MySampleData\games.csv', 'r') as csv_file:     
        reader = csv.reader(csv_file, delimiter=',')
        # Skip header row
        next(reader)
        rowNum=1
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
            
           
            print(f"Inserting Row {rowNum} with data as imported below:-")
            
            print("gameId:", gameId)
            print("season:", season)
            print("week:", week)
            print("gameDate:", gameDate)
            print("gameTimeEastern:", gameTimeEastern)
            print("homeTeamAbbr:", homeTeamAbbr)
            print("visitorTeamAbbr:", visitorTeamAbbr)
            print("----------------------------------------------------------")
            
           
            cur = conn.cursor()
                
            cur.execute("INSERT INTO Games(gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) \
                            VALUES (:1, :2, :3,TO_DATE(:4, 'MM/DD/YYYY'), TO_TIMESTAMP(:5 || ' ' || :6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)",
                        (gameId, season, week, gameDate, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr))

            # Commit the transaction
            conn.commit()
            rowNum+=1
            # Close the cursor and connection
            cur.close()
            
            print("---------Insert Complete-------------------")


def assignIntNoneOrValue(val):
    if(val=='NA'):
        return None
    else:
        return int(val)
    
def assignStringNoneOrValue(val):
    if(val=='NA'):
        return None
    else:
        return val

def insertDataIntoPlayTable(conn):
    # Open CSV file and create a CSV reader object
    rowNum=0
    with open('.\MySampleData\plays.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        print(f"Inserting Rows......")
        
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
    
            conn.commit()
            cur.close()
            rowNum+=1
        print(f"Inserted {rowNum} rows.")
    
       

def insertDataIntoPlayersTable(conn):
    rowNum=0
    
    
    
    
if(__name__=="__main__"):
    conn = oracledb.connect(user="axm9433", password="Rameswar1996",
                            host="az6F72ldbp1.az.uta.edu", port=1523, service_name="pcse1p.data.uta.edu")
    if(conn):
        print(conn)
        print("Successfully connected to Oracle Database")
        print(conn.version)
        #insertDataIntoGamesTable(conn)
        #insertDataIntoPlayTable(conn)
        insertDataIntoPlayersTable(conn)
        
    conn.close()
    


