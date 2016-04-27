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
		#return "Session value set."
		#return session.keys()
		for item in session:
			print item
		return
	else:
		#return session['value']
		#return session.keys()
		for item in session:
			print item
		return

@app.route('/info/', methods=['GET'])
def getEngineInfo():
	return internal.getEngineInfo()

@app.route('/question/<int:base>/<int:qid>/<int:version>/', methods=['GET'])
def getQuestionMetadata(base, qid, version):
	return internal.getQuestionMetadata(base, qid, version)

@app.route('/question/<int:base>/<int:qid>/<int:version>/session/', methods=['POST'])
def start(base, qid, version):
	return internal.start(base, qid, version)

@app.route('/session/<int:sid>/response/', methods=['PUT'])
def process(sid):
	return internal.process(sid)

@app.route('/session/<int:sid>/', methods=['DELETE'])
def stop(sid):
	return internal.stop(sid)

if __name__ == '__main__':
	app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
	app.session_interface = BeakerSessionInterface()
	app.run(debug=True)
