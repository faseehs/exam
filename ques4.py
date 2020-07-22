import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="exam",
    auth_plugin='mysql_native_password'

)
cursor = db.cursor()
#cursor.execute("DROP TABLE IF EXISTS Eployeethree")
sql = """insert into Employeethree (
         EID ,
         ENAME ,
         EDESIG ,
         EMAIL ,
         ESAL ) values ('103','danie','testing','danie@gmail',25000)"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)

db.close()