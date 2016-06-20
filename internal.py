#!/usr/bin/env python

from psutil import *
import json

def getEngineInfo():
	return json.dumps({'name': '<string>', 'usedmemory': '<string>', 'activesessions': '<int>'})

def getQuestionMetadata(base, qid, version):
	return json.dumps({'scoring': {'marks':'<int>'}, 'plainmode': '<bool>'})

def start(base, qid, version):
	return json.dumps({'questionSession': '<sid>', 'XHTML': '<string>', 'CSS': '<string>', 'progressInfo': '<string>', 'resources': '[{content:<base64>,encoding:<string>,filename:<string>,mimetype:<string>}, ... ]'})

def process(sid):
	return json.dumps({'XHTML': '<string>', 'CSS': '<string>', 'progressInfo': '<string>', 'questionEnd': '<bool>', 'resources': '[{content: <base64>, encoding: <string>, filename: <string>, mimetype: <string>}, ... ]',
      'results': '[{questionLine: <string>, answerLine: <string>, actionSummary: <string>, attempts: <int>, scores: {<string>: <float>, ... }, customResults: {<string>: <string>, ... } }]'})

def stop(sid):
	return none
