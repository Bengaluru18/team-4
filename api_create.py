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
                dict2 = cf.insertAcademicsTable(con,[request.form['S_ID'],request.form['No_Aprogs'],request.form['Passper'],request.form['Comments']])
                return jsonify(dict2)
        except mdb.Error,e:
                dict2 = {'error':e,'error_no':'70'}
                return jsonify(dict2)
@app.route('/insertSurvey',methods=['POST'])
def surveyin():
        dict2={}
        try:
                con= mdb.connect('localhost','dbuser','Dbuser123!@','dbase_cwf');
                dict2 = cf.insertSurveyTable(con,[request.form['S_ID'],request.form['A_projs'],request.form['Status'],request.form['N_months']])
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
if __name__ == 'main':
        app.run( host='0.0.0.0')
	
