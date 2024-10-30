# Load support for mysql
import mysql.connector

# create mysql object
mydb = mysql.connector.connect(
    host="localhost",
    user="tweetabellen",
    password="tweetabellen",
    database="tweetabellen"
)

# create handler to database
cursor = mydb.cursor()
# send query to database
cursor.execute("SELECT * FROM eigenaars")
# get results from database
results = cursor.fetchall()
# process all results
for result in results:
    print(result)

print(results[0][1])