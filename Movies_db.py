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
            (2,'Bhuj: The Pride of India','Ajay Devgn',
            'Sonakshi Sinha',2021,' Abhishek Dudhaiya');'''
    
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

print("MOV_ID \t| MOV_NAME \t\t| LEAD_ACTOR \t\t| ACTRESS \t\t| YEAR \t\t| DIR_NAME")
print("-"*120)

for row in query:
   print(str(row[0])+"\t| "+row[1][:10]+"..\t\t| "+row[2][:10]+"..\t\t| "+row[3][:10]+"..\t\t| "+str(row[4])+"\t\t| "+row[5])
   print("-"*120)

print("\nQuerying records from all the rows successful! \n");

# Querying with parameter to select movies based on the actor's name.
query2 = conn.execute('''SELECT * FROM MOVIES 
                      WHERE
                      LEAD_ACTOR = "Ajay Devgn";''')

print("\nThe details of the movie with 'Lead Actor' as 'Ajay Devgn' is shown below - \n")

print("MOV_ID \t| MOV_NAME \t\t| LEAD_ACTOR \t\t| ACTRESS \t\t| YEAR \t\t| DIR_NAME")
print("-"*120)
for row in query2:
   print(str(row[0])+"\t| "+row[1][:10]+"..\t\t| "+row[2][:10]+"..\t\t| "+row[3][:10]+"..\t\t| "+str(row[4])+"\t\t| "+row[5])
   print("-"*120)

print("\nQuerying with parameter to select movie based on the actor's name successful! \n")

conn.commit()
conn.close()
