import mysql.connector

connect = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'default',
	database = 'logindb'
)

cursor = connect.cursor()

def access_db(data):
	try:
		cursor.execute("SELECT * FROM USERS WHERE USERNAME = binary %s AND PASSWD = BINARY %s", data)
		return (cursor.fetchone())
	except:
		False