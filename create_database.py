import sqlite3
import sys

def createLoginTable(con):
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS login")
		cur.execute("CREATE TABLE login(Username VARCHAR(30) PRIMARY KEY, Password VARCHAR(10))")

def insertLoginTable(con,username,password):
	with con:
		cur = con.cursor()
 		cur.execute("INSERT INTO login VALUES({},{})".format(username,password))
		return "Successful"
def retrieveLoginTable(con,username,password):
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM  login WHERE username={}".format(username))
		row = cur.fetchall()
		if row['password'] != password:
			return "Wrong Password"
		else:
			return "Success"
def createworkerTable(con):
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS worker")
		cur.execute("CREATE TABLE worker(FW_name VARCHAR(50), SchoolID VARCHAR(8) PRIMARY KEY, School_Name VARCHAR(50), Locality VARCHAR(30) Address VARCHAR(50), No_of Students INT, No_of_Girls INT, No_of_Boys INT, No_of_NGOs INT, Amount_old INT, District VARCHAR(20), state VARCHAR(20), region VARCHAR(20), block VARCHAR(20) )")

def insertworkerTable(con,x):
	if len(x) < 10:
		return "Not possible to isert"
	with con:
		cur= con.cursor()
		cur.execute("INSERT INTO worker VALUES({},{},{},{},{},{},{},{},{},{},{},{},{})".format(*x))
		return "Successful"
def retrieveSchoolTable(con,SchoolId):
	if SchoolId == '':
		return "please enter the schoolId"
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE SchoolID={}".format(SchoolID))
		rows = cur.fetchall()
		return rows
def retirveDistrict(con,district):
	if district == '':
		return "please select a district"
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE district={} ".format(district))
		rows = cur.fetchall()
		return rows
