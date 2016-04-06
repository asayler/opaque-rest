'''
/info/                                          GET     getEngineInfo()
/question/<base>/<qid>/<version>/               GET     getQuestionMetadata(<base>, <qid>, <version>)
/question/<base>/<qid>/<version>/session/       POST    start(<base>, <qid>, <version>)
/session/<sid>/response/                        PUT     process(<sid>)
/session/<sid>/                                 DELETE  stop(<sid>)
'''
#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

'''
Request
	 None
Response
	'name': '<string>',
	'usedmemory': '<string>', (optional)
	'activesessions': <int> (optional)
'''
@app.route('/info/')
def getEngineInfo():
	return 'Info'

'''
Request
	None
Response
{ 
'scoring': {
	   'marks': <int>
	 },
'plainmode': <true|false>
}
'''
@app.route('/question/<base>/<qid>/<version>/')
def getQuestionMetadata(base, qid, version):
	return 'Question metadata'

'''
Request
	'randomseed': <int>,
	'userid': '<uid>',
	'language': '<string>',
	'passKey': '<string>',
	'preferredbehavior': '<string>'
Response
	{
	'questionSession': '<sid>',
	'XHTML': '<string>',
	'CSS': '<string>',
	'progressInfo': '<string>',
	'resources': [
		     {
		       'content': '<base64>',
		       'encoding': '<string>',
		       'filename': '<string>'
		       'mimetype': '<string>'
		     },
		     ...
		   ]
	}
'''
@app.route('/question/<base>/<qid>/<version>/session/')
def start(base, qid, version):
	return 'Start'

'''
Request
	{
	'key1': 'val1',
	'key2': 'val2',
	...
	}
Response
	{
	'XHTML': '<string>',
	'CSS': '<string>',
	'progressInfo': '<string>',
	'questionEnd': <true|false>
	'resources': [
		     {
		       'content': '<base64>',
		       'encoding': '<string>',
		       'filename': '<string>'
		       'mimetype': '<string>'
		     },
		     ...
		   ]
	'results': [
		   {
		     'questionLine': '<string>',
		     'answerLine': '<string>',
		     'actionSummary': '<string>',
		     'attempts': <int>,
		     'scores': {
				 '<string>': <float>,
				 ...
			       }
		     'customResults': {
					'<string>': <string>,
					 ...
				       }
		   }
		 ]
	}
'''
@app.route('/session/<sid>/response/')
def process(sid):
	return 'Process'

'''
Request
	None
Response
	None
'''
@app.route('/session/<sid>/')
def stop(sid):
	return 'Stop'

if __name__ == '__main__':
	app.run()
