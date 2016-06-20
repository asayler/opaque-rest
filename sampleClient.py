#!/usr/bin/env python

import requests
import pprint
import click

@click.group()
@click.option('--url', default=None, help="OPAQUE-Rest Base URL")
@click.pass_context
def cli(url):
	global baseURL
	if not baseURL:
		baseURL = click.prompt("URL", type=str)
	if baseURL[len(baseURL)-1] == '/':
		baseURL = baseURL[:len(baseURL)-1]
	menuMain()

choice = ""
baseURL = ""

def getEngineInfo():
	global baseURL
	url = baseURL + "/info"
	try:
		args = ""
		r = requests.get(url, params=args)
	except requests.exceptions as e:
		x = 0 #Stub holder

def getQuestionMetadata():
	global baseURL
        try:
                args = ""
                r = requests.get(url, params=args)
        except requests.exceptions as e:
                x = 0 #Stub holder

def start():
	global baseURL
        try:
                args = ""
                r = requests.get(url, params=args)
        except requests.exceptions as e:
                x = 0 #Stub holder

def process():
	global baseURL
        try:
                args = ""
                r = requests.get(url, params=args)
        except requests.exceptions as e:
                x = 0 #Stub holder

def stop():
	global baseURL
        try:
                args = ""
                r = requests.get(url, params=args)
        except requests.exceptions as e:
                x = 0 #Stub holder

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

def menuMain():
	global choice
	while True:
		if printMenu():
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
		else:
			print "Error: Not valid option"

if __name__ == '__main__':
	cli()
