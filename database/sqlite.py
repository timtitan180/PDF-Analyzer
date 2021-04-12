import sqlite3


database = "pdf_analyzer.db"
connection = sqlite3.connect(database)

connection.execute('''CREATE TABLE PDF ANALYZER
(FILE_NAME TEXT NOT NULL,PDF_ANALYSIS TEXT NOT NULL);''')
connection.commit()


connection.close()



