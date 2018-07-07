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
		cur.execute("INSERT INTO worker VALUES({},{},{},{},{},{},{},{},{},{},{},{},{})".format(tuple(x)))
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
def retirveBlock(con,block):
        if block == '':
                return "please select a block"
        with con:
                cur=con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT * FROM worker WHERE block={} ".format(block))
                rows = cur.fetchall()
                return rows
def retrieveRegion(con,region):
	if not region:
		return "please select a region"
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE region={}".format(region))	
		rows = cur.fetchall()
		return rows
def createFacilitiesTable(con):
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS Facilities")
		cur.execute("CREATE TABLE Facilties(SchoolID INT PRIMARY KEY, Sports_facilities INT, Construction INT Child_fac INT, Meals INT )")
	
def InsertFacilitiesTable(con,a):
	for i in a:
		if  i < 0  or  i > 10:
			return "Invalid Input"
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO Facilities VALUES({},{},{},{},{})".format(tuple(a)))
		return "successful" 

def retriveFacilitiesTable(con,SchoolID):
	if not SchoolID:
		return "please enter the SchoolId"
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM Facilities WHERE SchoolID={}".format(SchoolID))
		rows = cur.fetchall()
		return rows
def createAcademicsTable(con):
        with con:
                cur = con.cursor()
                cur.execute("DROP TABLE IF EXISTS Facilities")
                cur.execute("CREATE TABLE Facilties(SchoolID INT PRIMARY KEY, No_Academics_Progs INT, Pass_Percent INT, Comments VARCHAR(200))")
        
def InsertAcademicsTable(con,a):
        for i in a:
                if i < 0  or  i > 10:
                        return "Invalid Input"
        with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Facilities VALUES({},{},{},{})".format(tuple(a)))
                return "successful" 

def retriveAcademicsTable(con,SchoolID):
        if not SchoolID:
                return "please enter the SchoolId"
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT * FROM Facilities WHERE SchoolID={}".format(SchoolID))
                rows = cur.fetchall()
                return rows
def createSurveyTable(con):
        with con:
                cur = con.cursor()
                cur.execute("DROP TABLE IF EXISTS Facilities")
                cur.execute("CREATE TABLE Facilties(SchoolID INT PRIMARY KEY, Active_projects INT, Status INT,No_of_Months INT)")
        
def InsertSurveyTable(con,a):
        for i in a:
                if i < 0  or  i > 10:
                        return "Invalid Input"
        with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Facilities VALUES({},{},{},{})".format(tuple(a)))
                return "successful" 

def retriveSurveyTable(con,SchoolID):
        if not SchoolID:
                return "please enter the SchoolId"
        with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Facilities WHERE SchoolID={}".format(SchoolID))
                rows = cur.fetchall()
                return rows

