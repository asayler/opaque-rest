#!/usr/bin/env python

import requests

choice = ""

def getEngineInfo():
	print "werks?"

def getQuestionMetadata():
	return

def start():
	return

def process():
	return

def stop():
	return

def printMenu():
	global choice
	print "Select from the following options:"
	print " (1) getEngineInfo()"
	print " (2) getQuestionMetadata()"
	print " (3) start()"
	print " (4) process()"
	print " (5) stop()"
	print " (6) Exit"
	try:
		choice = input("")
		if isinstance(choice, int) and choice in [1,2,3,4,5,6]:
			return True
		else:
			return False
	except:
		return False

def main():
	global choice
	while True:
		if printMenu():
			'''
			if choice == 1:
				getEngineInfo()
			elif choice == 2:
				getQuestionMetadata()
			elif choice == 3:
				start()
			elif choice == 4:
				process()
			elif choice == 5:
				stop()
			else:
				exit()
			'''
			x = {
				1: getEngineInfo(),
				2: getQuestionMetadata(),
				3: start(),
				4: process(),
				5: stop(),
				6: exit()
			}.get(choice, exit())
		else:
			print "Error: Not valid option"
		print "wtf"
main()
