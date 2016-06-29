#!/usr/bin/python

import parameters as p
import functions as f
import classes

"""------------------------------------------------------------------------------------------------------------------------------
---------------- 	INITIATE WORLD
----------------
----------------
---------------------------------------------------"""


def initiate_organisations():
	#Creates a random set of new organisations for all three markets
	#First market is government
	create_org(0)
	for marketID in xrange(2):
		# for Social and Commercial market, initial number can be a range
		initial_num_ORGS = f.returnRandomInt(3,10)
		for num in xrange(initial_num_ORGS):
			create_org(marketID+1)
	f.debug(1, "Initiate Organisations")
	return 0


def create_org(marketID):
	org = classes.Organisation_CLASS(p.ORG_ID, marketID)
	p.ORG_ID += 1
	#initial stratey towards growth
	org.strategy = f.returnRandomInt(15,20)
	p.IDENTITY_MARKET.append(org)
	f.debug(1, "Create Organisation")
	return 0


"""------------------------------------------------------------------------------------------------------------------------------
---------------- 	INITIATE POPULATION
----------------
----------------
---------------------------------------------------"""


def initiate_population():
	f.debug(1, "Initiate Population")
	#first create the population
	for personID in xrange(p.NUM_POPULATION):
		create_person()
	#next initiate thier attributes
	for person in p.POPULATION:
		#initial number of friends - one direction only, so likly more
		for x in xrange(2):
			f.make_friend(person)
	return 0

def create_person():
	#Important to move the ID market along, person ID is same as position in list
	person = classes.Person_CLASS(p.PERSON_ID)
	p.PERSON_ID += 1
	p.POPULATION.append(person)	
	f.debug(1, "Created Person:"+str(person.displayPERSON())) 
	return person


"""------------------------------------------------------------------------------------------------------------------------------
---------------- 	INITIATE ACCOUNTS
----------------
----------------
---------------------------------------------------"""
def initiate_accounts():
	#initiate_govt_users()

	return 0

def initiate_govt_users():
	#this it the only Government Org
	org = p.IDENTITY_MARKET[0]
	for person in p.POPULATION:
		account = f.create_account(person,org)
	f.debug(1, "Initiate Government Users")
	return 0


