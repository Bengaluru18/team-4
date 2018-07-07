import sklearn
import matplotlib
import sys
import sqlite3
conn = sqlite3.connect('D:\jpmc.db')
cur = conn.cursor()
cur.execute("CREATE TABLE EDUCATION(ID INT PRIMARY KEY NOT NULL,TEACHER_NO INT,PRIMARY_STUDENTS INT,SECONDARY_STUDENTS INT,MALE_TEACHER_NO INT,FEMALE_TEACHER_NO INT,MEDIUM_INSTR VARCHAR(30),TEACHER_QUALITY INT,STUDENT_UNDERSTANDING INT,COMMENTS VARCHAR(70))")
cur.execute("CREATE TABLE INFRASTRUCTURE(ID INT PRIMARY KEY,NO_OF_CLASSROOM INT,NO_OF_BOARDS INT,NO_OF_BENCH INT,LIBRARY_P INT,LAB_P INT,LAB_LIB_Q INT,COMP INT,NO_OF_COMP INT,TOILET_COED INT,TOILET_Q INT,BUILDING_STAB INT,COMMENTS VARCHAR(70))")
cur.execute("CREATE TABLE HEALTH(ID INT PRIMARY KEY,NO_OF_PROG INT,FIRST_AID INT,MEDICINES INT,TRAINING INT,COUNSELLING INT,COMMENTS VARCHAR(70))")
cur.execute("CREATE TABLE STAKEHOLDER(ID INT PRIMARY KEY,TEACHER_TRAINING INT,PARENT_MEET INT,ALUMNI_ASSOC INT,SDC_SMC_INVOLVEMENT INT,COMMENTS)")
cur.execute("INSERT INTO EDUCATION VALUES({},{},{},{},{},{},{},{},{},{})".format(id1,teacherno,primary_students,sec_students,male_teachers,female_teachers,medium,teacher_q,student_u,comments))
cur.execute("INSERT INTO INFRASTRUCTURE({},{},{},{},{},{},{},{},{},{},{},{},{})".format(id1,no_of_classroom,no_of_boards,no_of_bench,library,lab,lquality,comp,no_of_comp,toilet_coed,toilet_q,building_stab,comments))
cur.execute("INSERT INTO HEALTH({},{},{},{},{},{},{})".format(id1,no_of_prog,firstaid,medicines,training,counselling,comments))
cur.execute("INSERT INTO STAKEHOLDER({},{},{},{},{},{})".format(id1,teacher_training,parent_meet,alumni_assoc,sdc_involve))