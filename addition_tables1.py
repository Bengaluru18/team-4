import sklearn
import matplotlib
import sys
import sqlite3
conn = sqlite3.connect('D:\jpmc.db')
cur = conn.cursor()
#COPY INTO ORIGINAL CODE FROM HERE
def create_general(con) :
    with con :
        cur=con.cursor()
        cur.execute("CREATE TABLE GENERAL(ID INT PRIMARY KEY,NAME VARCHAR(40),EXISTINGPROG INT,STRENGTH INT,NO_OF_GIRLS INT,NO_OF_BOYS INT,FUNDS INT,CLUSTER VARCHAR(30),BLOCK VARCHAR(30),REGION VARCHAR(30),STATE VARCHAR(30)")
        return "SUCCESSFUL"
def insert_general(con,x):
    cur.execute("INSERT INTO GENERAL({},{},{},{},{},{},{},{},{},{},{})".format(tuple(x)))
    return "SUCCESSFUL"
def retrieve_general(con,SchoolID) :
    if not SchoolID:
        return "please enter the SchoolId"
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM GENERAL WHERE SchoolID={}".format(SchoolID))
            rows = cur.fetchall()
            return rows
    
def create_education(con) :
    with con :
        cur=con.cursor()
       cur.execute("CREATE TABLE EDUCATION(ID INT PRIMARY KEY NOT NULL,TEACHER_NO INT,PRIMARY_STUDENTS INT,SECONDARY_STUDENTS INT,MALE_TEACHER_NO INT,FEMALE_TEACHER_NO INT,MEDIUM_INSTR VARCHAR(30),TEACHER_QUALITY INT,STUDENT_UNDERSTANDING INT,COMMENTS VARCHAR(70))")
       return "SUCCESSFUL"

def insert_education(con,x) :
    with con :
        cur=con.cursor()
        cur.execute("INSERT INTO EDUCATION VALUES({},{},{},{},{},{},{},{},{},{})".format(tuple(x)))
        return "SUCCESSFUL"
def retrieve_education(con,SchoolID) :
    if not SchoolID:
        return "please enter the SchoolId"
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM EDUCATION WHERE SchoolID={}".format(SchoolID))
            rows = cur.fetchall()
            return rows
def create_infrastructure(con) :
    with con :
        cur=con.cursor()
        cur.execute("CREATE TABLE INFRASTRUCTURE(ID INT PRIMARY KEY,NO_OF_CLASSROOM INT,NO_OF_BOARDS INT,NO_OF_BENCH INT,LIBRARY_P INT,LAB_P INT,LAB_LIB_Q INT,COMP INT,NO_OF_COMP INT,TOILET_COED INT,TOILET_Q INT,BUILDING_STAB INT,COMMENTS VARCHAR(70))")
        return "SUCCESSFUL"
def insert_infrastructure(con,x) :
    with con :
        cur=con.cursor()
        cur.execute("INSERT INTO INFRASTRUCTURE({},{},{},{},{},{},{},{},{},{},{},{},{})".format(tuple(x)))
        return "SUCCESSFUL"
def retrieve_infrastructure(con,SchoolID) :
    if not SchoolID:
        return "please enter the SchoolId"
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM INFRASTRUCTURE WHERE SchoolID={}".format(SchoolID))
            rows = cur.fetchall()
            return rows
def create_health(con) :
    with con :
        cur=con.cursor()
        cur.execute("CREATE TABLE HEALTH(ID INT PRIMARY KEY,NO_OF_PROG INT,FIRST_AID INT,MEDICINES INT,TRAINING INT,COUNSELLING INT,COMMENTS VARCHAR(70))")
        return "SUCCESSFUL"

def insert_health(con,x) :
    with con :
        cur=con.cursor()
        cur.execute("INSERT INTO HEALTH({},{},{},{},{},{},{})".format(tuple(x)))
        return "SUCCESSFUL"
def retrieve_health(con,SchoolID) :
    if not SchoolID:
        return "please enter the SchoolId"
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM HEALTH  WHERE SchoolID={}".format(SchoolID))
            rows = cur.fetchall()
            return rows
def create_stakeholder(con) :
    with con :
        cur=con.cursor()
        cur.execute("CREATE TABLE STAKEHOLDER(ID INT PRIMARY KEY,TEACHER_TRAINING INT,PARENT_MEET INT,ALUMNI_ASSOC INT,SDC_SMC_INVOLVEMENT INT,COMMENTS)")
        return "SUCCESSFUL"
def insert_stakeholder(con,x) :
    with con :
        cur=con.cursor()
        cur.execute("INSERT INTO STAKEHOLDER({},{},{},{},{},{})".format(tuple(x)))
def retrieve_stakeholder(con,SchoolID) :
    if not SchoolID:
        return "please enter the SchoolId"
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM HEALTH  WHERE SchoolID={}".format(SchoolID))
            rows = cur.fetchall()
            return rows
