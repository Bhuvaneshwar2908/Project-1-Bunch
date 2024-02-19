import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='Bhuvan29@2001',database='photography',autocommit=True)
cursor = mydb.cursor()  
cursor.execute("insert into login (username , password) values( 'bhuvan', 'bhuvan29@')")