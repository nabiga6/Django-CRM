import mysql.connector

#Connection to Database

dataBase = mysql.connector.connect(
	host ='localhost',
	user = 'root',
	passwd = ''

	)

#Creation ou préparation du curseur

cur = dataBase.cursor()

#Creation de la base de données
cur.execute("CREATE DATABASE elderco")

print("All done!")