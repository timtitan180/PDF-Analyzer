import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="pdfanalyzerschema"
)

database_cursor = mydb.cursor()

