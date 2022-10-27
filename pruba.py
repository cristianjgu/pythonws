from flask import Flask, request
from main import *

import json
app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
	return "hola"

@app.route('/pruba',methods=['GET'])
def eje():
	query_params = request.args
	value = {
		"firstName": query_params,
		"lastName": "Gupta",
		"hobbies": ["playing", "problem solving", "coding"],
		"age": 20
	}

	return json.dumps(value)
@app.route('/getData',methods=['GET'])
def eje3():
	query_params = request.args
	value={"return": [
		{
			"item": [
				{
					"item": [
						"label:Registro",
						"color:(255,255,255)",
						"background:(0,0,0)",
						"type:titulo"
					]
				},
				{
					"item": [
						"text:Log",
						"label:log",
						"type:textarea"
					]
				}
			]
		},
		{
			"item": [
				{
					"item": [
						"label:Petición",
						"color:(255,255,255)",
						"background:(0,0,0)",
						"type:titulo"
					]
				},
				{
					"item": [
						"text:Get Process",
						"label:Discovery",
						"type:button",
						"WS:Discover"
					]
				}
			]
		}
	]}
	return json.dumps(value)
@app.route('/Discover2',methods=['GET'])
def eje4():
	query_params = request.args
	print(query_params)
	grafo = ['Titulo:Grafos']
	for ele in display():
		grafo.append(ele)
	value={"return": [
		{
		"item": grafo
		}]
	}
	
	return json.dumps(value)
if __name__=="__main__":
	app.run(port = 5000, debug=False)