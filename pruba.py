from flask import Flask, request
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
	value={"return": [
		{
		"item": [
			'Titulo:Grafos',
			'digraph G {nodesep=0.5;rankdir=LR;\n1 [label="g";xlp="4,1 0";xlabel="[B2,C-1]";shape=box;penwidth=3,style=filled,color="black",fillcolor="#BFD1D2",fontsize=18];\nPini [style=filled,color="chartreuse2"];\nPfin [style=filled,color="firebrick1"];1(arrow)Pfin\nPini(arrow)1}',
			'digraph G {nodesep=0.5;rankdir=LR;\nB0(arrow)B2[color="#00ff00"];B2(arrow)B1[color="#00ff00"];B0[shape=box;style=filled,fontsize=18,xlabel="[ALPHA]"];\nB1[shape=box;style=filled,fontsize=18,xlabel="[BETA]"];\nB2[shape=box;style=filled,fontsize=18,xlabel="[g]"];}'
  		]
		}]
	}
	return json.dumps(value)
if __name__=="__main__":
	app.run(port = 5000, debug=False)