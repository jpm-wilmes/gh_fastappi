# Testprogram for a rudimentory menu
# extra support for clearing screen prior to obtaining dbase data
import os
os.system('cls')

import mysql.connector

def mysqluse(qry):
   # create mysql object
    mydb = mysql.connector.connect(
        host="localhost",
        user="tweetabellen",
        password="tweetabellen",
        database="tweetabellen"
    )
    # show qry for check on syntax
    print(qry)
    # create handler to database
    cursor = mydb.cursor()
    # send query to database
    cursor.execute(qry)
  
    results = cursor.fetchall()
    mydb.commit()
    return results

def addnaam():
   eigenaar = input("Naam:")
   bijnaam = input("Bijnaam:")
   qry = "INSERT INTO eigenaars (eigenaar, bijnaam) VALUES (\"" + eigenaar + "\",\"" + bijnaam +"\");"

   result=mysqluse(qry)
   print(result)
   
   print("Student " + eigenaar + " toegevoegd")
    
def delnaam():
   eigenaar = input("Te verwijderen eigenaar:")
   qry = "DELETE FROM eigenaars WHERE eigenaar = \"" + eigenaar + "\";"
   result=mysqluse(qry)
   print(result)

   print("Student " + eigenaar + " verwijderd")
   
def updatenaam():
   #    update contains 3 sections: get original data, ask new data and store new data

   eigenaar = input("Te wijzigen eigenaar:")
   #    find eigenaar
   qry = "SELECT * from eigenaars WHERE eigenaar = \"" + eigenaar + "\";"
   results=mysqluse(qry)
   print(results)
   oudeeigenaar = results[0][1]
   oudebijnaam = results[0][2]
   #    aks new data while presenting old data
   eigenaar = input("Geef de nieuwe naam voor: " + oudeeigenaar + ": ")
   bijnaam = input("Geef de nieuwe bijnaam voor: " + oudebijnaam + ": ")
   #   store new data
   qry = "UPDATE eigenaars SET eigenaar = \"" + eigenaar + "\" , bijnaam = \"" + bijnaam + "\" WHERE eigenaar = \"" + oudeeigenaar + "\";" 
   results=mysqluse(qry)

   print("Student aangepast")

# Main program
ans=True
# Loop until option 4
while ans: 
    print("""
    1.Voeg een naam toe
    2.Verwijder een naam
    3.Wijzig een naam
    4.Einde
    """)
    ans=input("Maak een keuze 1-4:")
    if ans=="1":
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
