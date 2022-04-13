import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('MOVIE.db')
print("Connection Successful! \n")

# Creating a new table (Movies)
table_creation = '''CREATE TABLE MOVIES
                    (MOV_ID INT PRIMARY KEY NOT NULL,
                    MOV_NAME TEXT NOT NULL,
                    LEAD_ACTOR TEXT NOT NULL,
                    ACTRESS TEXT NOT NULL,
                    RELEASE_YEAR INT NOT NULL,
                    DIR_NAME TEXT NOT NULL);'''

conn.execute(table_creation)
print("Table Created Successfully! \n")


# Inserting data into Movies table
row1 = '''INSERT INTO MOVIES 
            (MOV_ID,MOV_NAME,LEAD_ACTOR,ACTRESS,RELEASE_YEAR,DIR_NAME)
            VALUES
            (1,'The Kashmir Files','Mithun Chakraborty',
            'Pallavi Joshi',2022,'Vivek Agnihotri');'''

row2 = '''INSERT INTO MOVIES 
            (MOV_ID,MOV_NAME,LEAD_ACTOR,ACTRESS,RELEASE_YEAR,DIR_NAME)
            VALUES
            (2,'83','Ranveer Singh',
            'Deepika Padukone',2021,'Kabir Khan');'''
    
row3 = '''INSERT INTO MOVIES 
            (MOV_ID,MOV_NAME,LEAD_ACTOR,ACTRESS,RELEASE_YEAR,DIR_NAME)
            VALUES
            (3,'Shershaah','Sidharth Malhotra',
            'Kiara Advani',2021,'Vishnuvardhan');'''
        
row4 = '''INSERT INTO MOVIES 
            (MOV_ID,MOV_NAME,LEAD_ACTOR,ACTRESS,RELEASE_YEAR,DIR_NAME)
            VALUES
            (4,'Uri: The Surgical Strike','Vicky Kaushal',
            'Yami Gautam',2019,'Aditya Dhar');'''
            
row5 = '''INSERT INTO MOVIES 
            (MOV_ID,MOV_NAME,LEAD_ACTOR,ACTRESS,RELEASE_YEAR,DIR_NAME)
            VALUES
            (5,'Mission Mangal','Akshay Kumar',
            'Vidya Balan',2019,'Jagan Shakti');'''
    
conn.execute(row1)
conn.execute(row2)
conn.execute(row3)
conn.execute(row4)
conn.execute(row5)


print("Records Entered Into the Movie table successfully! \n")


# Querying all rows from the Movies table
query = conn.execute('''SELECT MOV_ID,MOV_NAME,LEAD_ACTOR,
                     ACTRESS,RELEASE_YEAR,DIR_NAME 
                     FROM MOVIES''')
for row in query:
   print("MOV_ID = ", row[0])
   print("MOV_NAME = ", row[1])
   print("LEAD_ACTOR = ", row[2])
   print("ACTRESS = ", row[3])
   print("RELEASE_YEAR = ", row[4])
   print("DIR_NAME = ", row[5] ,"\n")

print("Querying records from all the rows successful! \n");

# Querying with parameter to select movies based on the actor's name.
query2 = conn.execute('''SELECT * FROM MOVIES 
                      WHERE
                      LEAD_ACTOR = "Ranveer Singh";''')
print("The details of the movie with 'Lead Actor' as 'Ranveer Singh' is shown below - ")
for row in query2:
   print("MOV_ID = ", row[0])
   print("MOV_NAME = ", row[1])
   print("LEAD_ACTOR = ", row[2])
   print("ACTRESS = ", row[3])
   print("RELEASE_YEAR = ", row[4])
   print("DIR_NAME = ", row[5] ,"\n")
   
conn.commit()
conn.close()
