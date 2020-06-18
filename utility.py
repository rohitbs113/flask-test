from flask import jsonify

def create_json_response(message, data):
	if data and isinstance(data, Exception):
		data = ' : '.join([str(data.__class__.__name__), str(data)])
	json_response = jsonify({
								'status': {'message': message},
								'data': data
							})
	return json_response
	