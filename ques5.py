import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="exam",
    auth_plugin='mysql_native_password'

)
cursor = db.cursor()

sql ="""select count(edesig) from employeethree
         """
try:
    cursor.execute(sql)
    data=cursor.fetchone()
except Exception as e:
    print(e.args)

db.close()