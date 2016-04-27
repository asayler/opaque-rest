#!/usr/bin/env python

from psutil import *
import json

def getEngineInfo():
	return json.dumps({'name': '<string>', 'usedmemory': virtual_memory().total, 'activesessions': '<int>'})

def getQuestionMetadata(base, qid, version):
	return json.dumps({'scoring': {'marks': 9000}, 'plainmode': True})

def start(base, qid, version):
	return "Start"

def process(sid):
	return "Process"

def stop(sid):
	return "Stop"
