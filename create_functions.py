import MySQLdb as mdb
import sys
dict1 = {'result':'success','error':0}
def createLoginTable(con):
	with con:
		cur = con.cursor()
		#cur.execute("DROP TABLE IF EXISTS `login`")
		cur.execute("CREATE TABLE login(Username VARCHAR(30) PRIMARY KEY, Password VARCHAR(10))")

def retrieveLoginTable(con,username,password):
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		str1="SELECT * FROM  login WHERE username='{}'".format(username)
		print '--------------------------------------------------------------------------------'
		print str1
		cur.execute(str1)
		row = cur.fetchall()
		print '-------------------------------------------------------------------------------jbh--------------------------'
		print row
		if row[0]['Password'] != str(password):
			dict1['result'] = None
			dict1['error'] = "Password invalid"
			return dict1
		return dict1 
def createworkerTable(con):
	with con:
		cur = con.cursor()
		#cur.execute("DROP TABLE IF EXISTS `worker`")
		cur.execute("CREATE TABLE worker(SchoolID VARCHAR(8) PRIMARY KEY, School_Name VARCHAR(50), Locality VARCHAR(30), No_of_Students INT, No_of_Girls INT, No_of_Boys INT, No_of_NGOs INT, Amount_old INT, District VARCHAR(20), state VARCHAR(20), region VARCHAR(20), block VARCHAR(20) )")

def insertworkerTable(con,x):
	print x
	if len(x) < 12:
		return "Not possible to insert"
	with con:
		print '--------------------------------------------------------'
		print len(x)
		y = []
		for i in x:
			y.append(str(i))
		print y 
		cur= con.cursor()
		cur.execute("INSERT INTO worker VALUES('{0}','{1}','{2}',{3},{4},{5},{6},{7},'{8}','{9}','{10}','{11}')".format(*y))
		return dict1
def retrieveSchoolTable(con,SchoolId):
	if SchoolId == '':
		dict1['error']='invalid schoolid'
		return dict1
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE SchoolID='{}'".format(SchoolId))
		rows = cur.fetchall()
		dict1['result'] = rows
		return dict1
def retirveDistrict(con,district):
	if district == '':
		dict1['error']='invalid district'
		return dict1
	with con:
		cur=con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE district='{}'".format(district))
		rows = cur.fetchall()
		dict1['result'] = rows
		return dict1
def retirveBlock(con,block):
        if block == '':
	        dict1['error']="Invaild"
	        return dict1
        with con:
                cur=con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT * FROM worker WHERE block='{}'".format(block))
                rows = cur.fetchall()
                dict1['result'] = rows
                return dict1
def retrieveRegion(con,region):
	if not region:
		dict1['error']="Invalid"
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM worker WHERE region='{}'".format(region))	
		rows = cur.fetchall()
		dict1['result'] = rows
		return dict1
def createFacilitiesTable(con):
	with con:
		cur = con.cursor()
		#cur.execute("DROP TABLE IF EXISTS `Facilities`")
		cur.execute("CREATE TABLE Facilties(SchoolID INT PRIMARY KEY, Sports_facilities INT, Construction INT,Child_fac INT, Meals INT )")
	
def InsertFacilitiesTable(con,a):
	for i in range(1,len(a)):
		if  int(a[i]) < 0  or  int(a[i]) >10:
			return "Invalid Input"
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO Facilties VALUES('{0}',{1},{2},{3},{4})".format(*a))
		return dict1 

def retriveFacilitiesTable(con,SchoolID):
	if not SchoolID:
		dict1['error']='Invalid'
		return dict1
	with con:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute("SELECT * FROM Facilties WHERE SchoolID='{}'".format(SchoolID))
		rows = cur.fetchall()
		dict1['result'] = rows
		return dict1
def createAcademicsTable(con):
        with con:
                cur = con.cursor()
                #cur.execute("DROP TABLE IF EXISTS `Academics`")
                cur.execute("CREATE TABLE Academics(SchoolID INT PRIMARY KEY, No_Academics_Progs INT, Pass_Percent INT, Comments VARCHAR(200))")
        
def InsertAcademicsTable(con,a):
       for i in a:
                if i < 0  or  i > 10:
                        dict1['error'] = 'Invalid'
                        return dict1
       with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Academics VALUES('{0}',{1},{2},{3})".format(*a))
                return dict1

def retriveAcademicsTable(con,SchoolID):
        if not SchoolID:
                dict1['error']="please enter the SchoolId"
                return dict1
        with con:
                cur = con.cursor(mdb.cursors.DictCursor)
                cur.execute("SELECT * FROM Academics WHERE SchoolID='{}'".format(SchoolID))
                rows = cur.fetchall()
                dict1['result'] = rows
                return dict1
def createSurveyTable(con):
        with con:
                cur = con.cursor()
                #cur.execute("DROP TABLE IF EXISTS `Survey`")
                cur.execute("CREATE TABLE Survey(SchoolID INT PRIMARY KEY, Active_projects INT, Status INT,No_of_Months INT)")
        
def InsertSurveyTable(con,a):
        for i in a:
                if i < 0  or  i > 10:
                        dict1['error'] = "Invalid"
                        return dict1
        with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Survey VALUES('{0}',{1},{2},{3})".format(*a))
                return dict1 

def retriveSurveyTable(con,SchoolID):
        if not SchoolID:
                return "please enter the SchoolId"
        with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Survey WHERE SchoolID='{}'".format(SchoolID))
                rows = cur.fetchall()
                dict1['result'] = rows
                return dict1
