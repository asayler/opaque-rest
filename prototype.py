#!/usr/bin/env python

from flask import request
from flask import Flask

import base64
import json

app = Flask(__name__)

@app.route('/info/', methods=['GET', 'POST'])
def getEngineInfo():
	#return 'Info'

	#usedmemory and activesessions are optional. Return them with the json if they are flagged in the request
	return json.dumps({'name': '<string>', 'usedmemory': '<string>', 'activesessions': '<int>'})

@app.route('/question/<int:base>/<int:qid>/<int:version>/', methods=['GET', 'POST'])
def getQuestionMetadata(base, qid, version):
	return 'Question metadata'

@app.route('/question/<int:base>/<int:qid>/<int:version>/session/', methods=['GET', 'POST'])
def start(base, qid, version):
	#return 'Start'
	return '%s %s %s' % (base, qid+1, version)

@app.route('/session/<int:sid>/response/', methods=['PUT'])
def process(sid):

	for arg in request.args:
		print arg, request[arg]
	return 'Process'

@app.route('/session/<int:sid>/', methods=['DELETE'])
def stop(sid):
	return 'Stop'

if __name__ == '__main__':
	app.run()
