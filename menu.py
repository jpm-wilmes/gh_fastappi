# Testprogram for a rudimentory menu
# extra support for clearing screen prior to obtaining dbase data
import os



# load support for mysql
import mysql.connector

# database basic funtion
# param: query to database
# result: query results (array)
def mysqluse(qry):
   # create mysql object
    mydb = mysql.connector.connect(
        host="localhost",
        user="tweetabellen",
        password="tweetabellen",
        database="tweetabellen"
    )
    # show qry for check on syntax
    print(qry, file=open('output.txt', 'a'))
    # create handler to database
    cursor = mydb.cursor()
    # send query to database
    cursor.execute(qry)

    results = cursor.fetchall()
    mydb.commit()
    return results

# list the content of the table eigenaars CRUD READ
def listnaam():
  qry = "SELECT eigenaar, bijnaam FROM eigenaars"
  result = mysqluse(qry)
  for eigenaar in result:
    print(eigenaar[0])

# add a new eigenaar to the table eigenaars CRUD CREATE
def addnaam():
   eigenaar = input("Naam:")
   bijnaam = input("Bijnaam:")
   qry = "INSERT INTO eigenaars (eigenaar, bijnaam) VALUES (\"" + eigenaar + "\",\"" + bijnaam +"\");"

   result=mysqluse(qry)
   print(result, file=open('output.txt', 'a'))
   
   print("Student " + eigenaar + " toegevoegd")

# remove eigenaar from table eigenaars CRUD DELETE    
def delnaam():
   eigenaar = input("Te verwijderen eigenaar:")
   qry = "DELETE FROM eigenaars WHERE eigenaar = \"" + eigenaar + "\";"
   result=mysqluse(qry)
   print(result, file=open('output.txt', 'a'))

   print("Student \"" + eigenaar + "\" verwijderd")

# modify eigenaar in table eigenaars CRUD UPDATE   
def updatenaam():
   #    update contains 3 sections: get original data, ask new data and store new data

   eigenaar = input("Te wijzigen eigenaar:")
   #    find eigenaar
   qry = "SELECT * from eigenaars WHERE eigenaar = \"" + eigenaar + "\";"
   results=mysqluse(qry)
   # print output to to testlog
   print(results, file=open('output.txt', 'a'))
   oudeeigenaar = results[0][1]
   oudebijnaam = results[0][2]
   #    aks new data while presenting old data
   eigenaar = input("Geef de nieuwe naam voor: " + oudeeigenaar + ": ")
   bijnaam = input("Geef de nieuwe bijnaam voor: " + oudebijnaam + ": ")
   #   store new data
   qry = "UPDATE eigenaars SET eigenaar = \"" + eigenaar + "\" , bijnaam = \"" + bijnaam + "\" WHERE eigenaar = \"" + oudeeigenaar + "\";" 
   results=mysqluse(qry)

   print("Student " + eigenaar + " aangepast")

# Main program
ans=True
# Loop until option 4
while ans: 
    print("""
    0. Laat namen zien
    1. Voeg een naam toe
    2. Verwijder een naam
    3. Wijzig een naam
    4. Einde
    """)
    ans=input("Maak een keuze 0-4: ")
    if ans=="0":
      listnaam()
    elif ans=="1":
      addnaam()
    elif ans=="2":
      delnaam()
    elif ans=="3":
      updatenaam()
    elif ans=="4":
      print("\nBedankt") 
      ans = None
    else:
       print("\nFoutieve invoer, probeer opnieuw")
