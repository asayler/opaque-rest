#!/usr/bin/env python

from flask import Flask, session, request
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

import internal
import base64
import json

app = Flask(__name__)

session_opts = {
	'session.type': 'ext:memcached',
	'session.url': '127.0.0.1:11211',
	'session.data_dir': './cache',
}

class BeakerSessionInterface(SessionInterface):
	def open_session(self, app, request):
		session = request.environ['beaker.session']
		return session

	def save_session(self, app, session, response):
		session.save()

@app.route('/')
def index():
	if not session.has_key('value'):
		session['value'] = 'Save in session'
		return "Session value set."
	else:
		return session['value']
@app.route('/info/', methods=['GET', 'POST'])
def getEngineInfo():
	#return 'Info'

	#usedmemory and activesessions are optional. Return them with the json if they are flagged in the request
	#return json.dumps({'name': '<string>', 'usedmemory': '<string>', 'activesessions': '<int>'})
	return internal.engineStatus()

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
	app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
	app.session_interface = BeakerSessionInterface()
	app.run(debug=True)
