'''
A Python Script to load the records available in given csv to the created tables in oracle db.
'''
import oracledb
import csv
from datetime import datetime

def insertData(conn):
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

        
        
'''
        # Get the first row of the CSV file
        row = next(csv_reader)
        row = next(csv_reader)
    
        # Create a cursor object
        cur = conn.cursor()
    
        print(row[1])
        
        # Insert the row into the Games table
        gameId = int(row[0])
        season = int(row[1])
        week = int(row[2])
        gameDate = row[3]
        gameTimeEastern = row[4]
        homeTeamAbbr = row[5]
        visitorTeamAbbr = row[6]
        
        print("gameId:", gameId)
        print("season:", season)
        print("week:", week)
        print("gameDate:", gameDate)
        print("gameTimeEastern:", gameTimeEastern)
        print("homeTeamAbbr:", homeTeamAbbr)
        print("visitorTeamAbbr:", visitorTeamAbbr)
        print("----------------------------------------------------------")
        
        
        cur.execute("INSERT INTO Games(gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) \
                    VALUES (:1, :2, :3,TO_DATE(:4, 'MM/DD/YYYY'), TO_TIMESTAMP(:5 || ' ' || :6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)",
                (gameId, season, week, gameDate, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr))

        # Commit the transaction
        conn.commit()
    
        # Close the cursor and connection
        cur.close()
    
    
    
    
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
            
            sql = f"INSERT INTO Games (gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr) " \
                  f"VALUES (:1, :2, :3, TO_DATE(:4 || ' ' || :5, 'MM/DD/YYYY HH:MI:SS AM'), :6, :7)"
            values = (gameId, season, week, gameDate, gameTimeEastern, homeTeamAbbr, visitorTeamAbbr)
            print(f"Inserting Row {rowNum} with data as imported below:-")
            
            print("gameId:", gameId)
            print("season:", season)
            print("week:", week)
            print("gameDate:", gameDate)
            print("gameTimeEastern:", gameTimeEastern)
            print("homeTeamAbbr:", homeTeamAbbr)
            print("visitorTeamAbbr:", visitorTeamAbbr)
            print("----------------------------------------------------------")
            
            #print("\n1.Insert the above data.\n2.Skip the above data.\n0.Exit The Loop.")
            #command=int(input())
            command=1
            if(command==1):
                # Execute SQL insert statement
                cursor = conn.cursor()
                cursor.execute(sql, values)
                cursor.close()
                print("---------Insert Complete-------------------")
            elif(command==2):
                continue
            else:
                return
'''
if(__name__=="__main__"):
    conn = oracledb.connect(user="axm9433", password="Rameswar1996",
                            host="az6F72ldbp1.az.uta.edu", port=1523, service_name="pcse1p.data.uta.edu")
    if(conn):
        print(conn)
        print("Successfully connected to Oracle Database")
        print(conn.version)
        insertData(conn)
    conn.close()
    


