from flask import Flask, redirect, render_template, request, url_for, session
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("index.html")

if __name__ == '__main__':
	app.run()