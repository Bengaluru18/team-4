import flask
import MySQLdb as mdb
#import requests
from flask import request, jsonify
app = flask.Flask(__name__)
app.config['DEBUG']=True
import create_functions as cf

@app.route('/loginretrieve',methods=['POST'])
def retrieveLogin():
	dict2={}
        try:
		con = mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.retrieveLoginTable(con,request.form["username"],request.form["pass"])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'40'}
                return jsonify(dict2)

@app.route('/insertworker',methods=['POST'])
def insertworker():
	print "gotit"
	dict2={}
	try:
		con = mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
		x=[]
		x.append(request.form["SchoolID"])
		x.append(request.form["S_name"])
		x.append(request.form["Locality"])
		x.append(request.form["S_No"])
		x.append(request.form["G_No"])
		x.append(request.form["B_No"])
		x.append(request.form["NGO_No"])
		x.append(request.form["Amount"])
		x.append(request.form["District"])
		x.append(request.form["State"])
		x.append(request.form["region"])
		x.append(request.form["block"])
		print x
		dict2 = cf.insertworkerTable(con,x)
		return jsonify(dict2)
	except mdb.Error, e:
		dict2 = {'error':e,'error_no':'50'}
		return jsonify(dict2)

@app.route('/retrieveSchool',methods=['GET'])
def school():
	dict2={}
	try:
		con=mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
		dict2 = cf.retrieveSchoolTable(con,request.args['SchoolId'])
		return jsonify(dict2)
	except mdb.Error, e:
		dict2 = {'error':e, 'error_no':'70'}
		return jsonify(dict2)

@app.route('/retrieveDistrict',methods=['GET'])
def district():
        dict2={}
        try:
                con=mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.retirveDistrict(con,request.args['District'])
                return jsonify(dict2)
        except mdb.Error, e:
                dict2 = {'error':e, 'error_no':'70'}
                return jsonify(dict2)

@app.route('/retrieveBlock',methods=['GET'])
def block():
        dict2={}
        try:
                con=mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.retirveBlock(con,request.args['Block'])
                return jsonify(dict2)
        except mdb.Error, e:
                dict2 = {'error':e, 'error_no':'70'}
                return jsonify(dict2)
@app.route('/retrieveRegion',methods=['GET'])
def region():
        dict2={}
        try:
                con=mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.retrieveRegion(con,request.args['Region'])
                return jsonify(dict2)
        except mdb.Error, e:
                dict2 = {'error':e, 'error_no':'70'}
                return jsonify(dict2)
@app.route('/insertfacilities',methods=['POST'])
def facilitiesin():
	dict2={}
	try:
		con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
		dict2 = cf.InsertFacilitiesTable(con,[request.form['S_ID'],request.form['Sports'],request.form['Constn'],request.form['Facilities'],request.form['Meals']])
		return jsonify(dict2)
	except mdb.Error,e:
		dict2 = {'error':e,'error_no':'70'}
		return jsonify(dict2)

@app.route('/insertacademics',methods=['POST'])
def academicsin():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.InsertAcademicsTable(con,[request.form['S_ID'],request.form['No_Aprogs'],request.form['Passper'],request.form['Comments']])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)
@app.route('/insertSurvey',methods=['POST'])
def surveyin():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.InsertSurveyTable(con,[request.form['S_ID'],request.form['A_projs'],request.form['Status'],request.form['N_months']])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)

@app.route('/insertEducation',methods=['POST'])
def eduin():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                x = []
		x.append(request.form['ID'])
		x.append(request.form['T_No'])
		x.append(request.form['P_stud'])
		x.append(request.form['S_stud'])
		x.append(request.form['MT_No'])
		x.append(request.form['FT_No'])
		x.append(request.form['Med_ist'])
		x.append(request.form['Teach_qual'])
		x.append(request.form['Stud_Un'])
		x.append(request.form['Comment'])
		dict2 = cf.insert_education(con,x)
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)
@app.route('/insertstake',methods=['POST'])
def stakein():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                x = []
                x.append(request.form['ID'])
                x.append(request.form['T_Train'])
                x.append(request.form['P_Meet'])
                x.append(request.form['Alum'])
                x.append(request.form['SDCInv'])
                x.append(request.form['Comments'])
                dict2 = cf.insert_stakeholder(con,x)
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)


@app.route('/insertinfra',methods=['POST'])
def infrain():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                x = []
                x.append(request.form['ID'])
                x.append(request.form['C_No'])
                x.append(request.form['B_No'])
                x.append(request.form['Ben_No'])
                x.append(request.form['Lib'])
                x.append(request.form['Lab'])
                x.append(request.form['Lab_Lib'])
                x.append(request.form['Comp'])
                x.append(request.form['Com_No'])
		x.append(request.form['Toil_Co'])
		x.append(request.form['Toil_Q'])
		x.append(request.form['Build'])
                x.append(request.form['Comment'])
                dict2 = cf.insert_infrastructure(con,x)
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)


@app.route('/retrievefacilities',methods=['GET'])
def facilitiesret():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
		dict2=cf.retriveFacilitiesTable(con,request.args['SchoolID'])
		return jsonify(dict2)
	except mdb.Error,e:
		dict2 = {'error':e, 'error_no':'90'}
		return jsonify(dict2)
@app.route('/retrieveacademics',methods=['GET'])
def academicsret():
        dict2={} 
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2=cf.retriveAcademicsTable(con,request.args['SchoolID'])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e, 'error_no':'100'}    
                return jsonify(dict2)   
@app.route('/retrieveSurvey',methods=['GET'])
def Surveyret():
        dict2={} 
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2=cf.retriveSurveyTable(con,request.args['SchoolID'])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e, 'error_no':'120'}    
                return jsonify(dict2)   

@app.route('/retrieveEdu',methods=['GET'])
def Eduret():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2=cf.retrieve_education(con,request.args['SchoolID'])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e, 'error_no':'120'}
                return jsonify(dict2)

@app.route('/retrieveInfra',methods=['GET'])
def infraret():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2=cf.retrieve_infrastructure(con,request.args['SchoolID'])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e, 'error_no':'120'}
                return jsonify(dict2)

@app.route('/retrievestake',methods=['GET'])
def stakeret():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2=cf.retrieve_stakeholder(con,request.args['SchoolID'])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e, 'error_no':'120'}
                return jsonify(dict2)


if __name__ == 'main':
        app.run( host='0.0.0.0')
	
