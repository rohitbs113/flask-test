from flask import Flask
from flask import render_template
from flask import request
from utility import *

app = Flask(__name__)

@app.route("/file/", defaults={'filename': 'file1'})
@app.route("/file/<filename>")
def home(filename):	
	params = request.args
	start, end = 0, 0
	if filename not in ['file1', 'file2', 'file3', 'file4']:
		return create_json_response("Error", "Filename is not correct")
	
	if params:		
		if "start" in params:
			start = int(params["start"])
		if "end" in params:
			end = int(params["end"])
	try:
		path = r"D:\AllPython\pythontestonflask\flask_test\data\{0}.txt".format(filename)
		if start and end:		
			with open(path, 'r', encoding="cp437") as f:
				data = f.read().split('\n')				
				data = data[start-1:end]
				data = "\n".join(data)
		
		else:		
			with open(path, 'r', encoding="cp437") as f:
				data = f.read()		
					
	except Exception as e:
		return create_json_response("Error", e)
		
	return render_template("home.html", data=data)
			
	
if __name__ == '__main__':
	app.run()