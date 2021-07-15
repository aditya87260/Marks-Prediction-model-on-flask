from flask import Flask
from sklearn.externals import joblib
model=joblib.load("model.pkl")
# __name__ == __main__
app = Flask(__name__)


from flask import Flask, render_template, redirect, request

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method=='POST':
        hours=float(request.form["hours"])
        marks=int(model.predict([[hours]]))

    return render_template("index.html",your_marks=marks) 
     







if __name__ == '__main__':
	# app.debug = True
	app.run(debug = True)
