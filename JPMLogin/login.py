from flask import Flask, redirect, render_template, request, url_for, session
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("index.html")
@app.route("/dash", methods=['GET', 'POST'])
def dash():
    if request.method=="GET":
        return render_template("dash.html")
@app.route("/report", methods=['GET', 'POST'])
def report():
    if request.method=="GET":
        return render_template("report.html")


if __name__ == '__main__':
	app.run()