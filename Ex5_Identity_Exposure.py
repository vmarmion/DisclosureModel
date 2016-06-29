#!/usr/bin/python

"""------------------------------------------------------------------------------------------------------------------------------
----------------	JUNE 2016
----------------	VINCENT MARMION
----------------	IDENTITIY EXPOSURE EXPERIMENT
---------------------------------------------------"""


from __future__ import division
from decimal import *
from initiate import *
from random import *
import math
import sys
import parameters as p
import functions as f
import output as o
import classes

"""------------------------------------------------------------------------------------------------------------------------------
----------------	USER ACTIONS
----------------
----------------
---------------------------------------------------"""


def joinOrg(person, org):

	numAcc = f.num_accounts(person,org.marketID)

	if f.already_account(person, org) == False:
		if numAcc < p.ENGAGE_MAX[org.marketID]:
			account = f.create_account(person, org)
			f.debug(0, "Person:%s Joining Org:%s " % (person.personID, org.orgID))
		else:
			f.debug(0, "TOO many accounts: NEED to SWITCH")
			switchOrg(person, org)	
	else: 
		f.debug(0, "Already an account with org "+str(org.orgID))
	return 0


def switchOrg(person, org):
	#still works on random utility, after selcting a random org
	f.shuffleList(person.accounts)
	switch = False
	marketID = org.marketID
	utility = f.calc_utility(person, org)
	for accountID in person.accounts:
		if switch == False:
			account = p.ACCOUNTS[accountID]
			if ((account.marketID == marketID) & (account.status == p.ACTIVE_1)):
				if f.calc_utility(person, p.IDENTITY_MARKET[account.orgID]) > utility:
					f.debug(0, "old account"+str(account.displayACCOUNT()))
					f.end_account(account)
					f.create_account(person, org)
					f.debug(1, "switched account"+str(person.displayPERSON()))
					switch = True
	return 0



def die(personID):
	dead = False
	person = p.POPULATION[personID]
	if person.status == p.ACTIVE_1:
		person.status = p.INACTIVE_0
		dead = True
		for accountID in person.accounts:
			account = p.ACCOUNTS[accountID]
			if account.status == ACTIVE_1:
				debug(0, "Dead Account: "+str(account.displayACCOUNT()))
				f.end_account(account)
		tempNet = list(person.network)
		for friendID in tempNet:
			f.lose_friend(person, friendID)
		debug(0, "DEAD: "+str(person.displayPERSON()))
	return dead


def born():
	create_person()
	person = p.POPULATION[-1]
	initiate_network(person.personID)
	f.debug(1, "BORN: "+ str(person.displayPERSON()))
	return 0


"""------------------------------------------------------------------------------------------------------------------------------
----------------	USER FUNCTIONS
----------------
----------------
---------------------------------------------------"""

def agePeople():
	for person in p.POPULATION:
		if person.status == p.ACTIVE_1:
			person.age += 1
		
	return 0

def maxAge():
	person = max(filter(lambda person: person.status == p.ACTIVE_1, p.POPULATION), key=lambda person: person.age)
	print "MAX AGE", person.age
	return person.age

def regenPOP():
	regen = math.ceil(p.NUM_POPULATION*0.15)
	for x in xrange(int(regen)):
		person = f.returnRandPerson()
		if ((person.age**4)/(p.MAXAGE**4)) > f.returnRandomReal():
			die(person.personID)
			born()
	return 0

def friends():
	#add friends at the start, and less at the end
	#absolute numbers i.e max 30
	#should be a funcion based on current friends and social organisations
	for person in p.POPULATION:
		if person.status == p.ACTIVE_1:
			if person.age < 30:
				f.make_friend(person)
			else:
				if len(person.network)-1 > 0:
					f.lose_friend(person, person.network[returnRandomInt(0, len(person.network)-1)])

	return 0

def updatePeople():
	regen = math.ceil(p.NUM_POPULATION*0.01)
	for x in xrange(int(regen)):
		person = f.returnRandPerson()
		joinOrg(f.returnRandPerson(), f.returnRandOrg())
	return 0

"""------------------------------------------------------------------------------------------------------------------------------
----------------	ORG FUNCTIONS
----------------
----------------
---------------------------------------------------"""

def updateAccounts():
	for account in p.ACCOUNTS:
		if account.status == p.ACTIVE_1:
			account.time += 1

def ageOrgs():
	for org in p.IDENTITY_MARKET:
		if org.status == p.ACTIVE_1:
			org.age += 1
	return 0

def updateOrgs(month, year):
	for org in p.IDENTITY_MARKET:
		if org.status == p.ACTIVE_1:
			orgMarketShare(org)
			orgReputation(org, month, year)
			updateOrgPolicy(org)
	return 0

def updateOrgPolicy(org):

	return 0



def orgMarketShare(org):
	num_users = len(org.users)
	onePerson = 100.0/p.NUM_POPULATION
	org.marketShare = onePerson * num_users
	return 0

def orgReputation(org, month, year):
	Hack = 1
	MarketShare = org.marketShare
	org.REPUTATION = (((year + month) * MarketShare) - (Hack * MarketShare))
	return 0

"""------------------------------------------------------------------------------------------------------------------------------
----------------	THREATS
----------------
----------------
---------------------------------------------------"""

def updateThreats():

	return 0


"""------------------------------------------------------------------------------------------------------------------------------
----------------	IDENTIFIERS
----------------
----------------
---------------------------------------------------"""




"""------------------------------------------------------------------------------------------------------------------------------
----------------	PLAY
----------------
----------------
---------------------------------------------------"""
def initiate():
	initiate_organisations()
	initiate_population()
	initiate_accounts()


def run_simulation():
	initiate()
	for year in xrange(p.YEARS):
		f.debug(1, ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
		for month in xrange(p.MONTHS):
			f.debug(1, "----- Year:"+str(year)+" Month:"+str(month))
			for step in xrange(p.STEPS):
				updatePeople()
				updateThreats()
			updateAccounts()
			updateOrgs(month, year)
		agePeople()
		friends()
		if year < p.YEARS-1:
			regenPOP()
		ageOrgs()
	
	
	f.debug(1, "run simulation")
	plotAges()
	o.writeCSV()
	return 0
	

def plotAges():
	alive = []
	dead = []
	friends  = []

	#for org in p.IDENTITY_MARKET:
	#	print org.displayORG()
	for person in p.POPULATION:
	#	print person.displayPERSON()
		if person.status == p.ACTIVE_1:
			alive.append(person.age)
			friends.append(len(person.network))
		else:
			dead.append(person.age)
	#for account in p.ACCOUNTS:
	#	print account.displayACCOUNT()
	#plt.hist(alive)
	#plt.show()
	#plt.hist(friends)
	#plt.show()
	return 0




	

run_simulation()

