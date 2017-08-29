from flask import Flask
from flask import render_template
from flask import request
from math import sqrt, log, sin, tan, cos


app = Flask (__name__)

@app.route("/", methods=["GET","POST"])
def lmao():
	calculator = ""
	if request.method == "POST":
		#print(request.form)
		calculator = request.form["calculator"]
		value = request.form["button"]
		if value == "=":
			calculator = eval(calculator)
		elif value == "C":
			calculator = calculator[:-1]
		elif value == "CE":
			calculator = ""
		elif value == "sin":
			calculator = sin(float(calculator))
		elif value == "tan":
			calculator = tan(float(calculator))
		elif value == "log":
			calculator = log(float(calculator))
		elif value == "sqrt":		 			
			calculator = sqrt(float(calculator))	
		else:	
			calculator = calculator + value

	return render_template("test.html", calculator=calculator)


if __name__=="__main__":
	app.run(debug=True, port=8085)	


