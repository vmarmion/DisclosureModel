#!/usr/bin/python

from random import *
import classes
import parameters as p

#-------------------FUNCTIONS-----------------------------------
#---------------------------------------------------------------

def returnRandomReal():
	num = uniform(0,1)
	return num

def returnRandomInt(start, stop):
	num = randint(start, stop)
	return num

def debug(on, text):
	if on == 1:
		print text
	return on

def shuffleList(listToShuffle):
	shuffle(listToShuffle)
	return 0

def findAccount(person, org):
	personID = person.personID
	orgID = org.orgID
	accountID = 0
	for account in p.ACCOUNTS:
		if ((account.personID == personID) & (account.orgID == orgID)):
			accountID = account.accountID
			print "found account", accountID
	return accountID

def friendsInOrg(person, org):
	users = org.users
	friends = person.network
	return len(set(friends).intersection(users))


def get_unique_friend(personID, network):
	found = False
	while found == False:
		friendID = returnRandomInt(0,len(p.POPULATION)-1)
		if friendID != personID:
			friend = p.POPULATION[friendID]
			if friend.status == p.ACTIVE_1:
				if friendID not in network:
					found = True
	return friendID

def calc_utility(person, org):
	#utility = friends + time
	print "FP", findAccount(person, org)
	account = p.ACCOUNTS[findAccount(person, org)]

	numFriendsInOrg = friendsInOrg(person, org)
	utility = (account.time * numFriendsInOrg)
	return utility

def create_account(person,org):
	account = classes.account_CLASS(p.ACCOUNT_ID)
	p.ACCOUNT_ID +=1
	
	account.personID = person.personID
	account.orgID = org.orgID
	account.marketID = org.marketID
	account.ID_disclosure = org.IDRequest
	
	
	org.users.append(person.personID)
	person.accounts.append(account.accountID)
	p.ACCOUNTS.append(account)
	debug(0, "Joined Account"+str(account.displayACCOUNT()))
	return account

def num_accounts(person, marketID):
	num = 0
	for accountID in person.accounts:
		account = p.ACCOUNTS[accountID]
		debug(0, "current accounts: "+ str(account.displayACCOUNT()))
		if ((account.marketID == marketID) & (account.status == p.ACTIVE_1)):
			num += 1
	return num


def returnRandOrg():
	#if no active org, then this is a problem
	found = False
	while found == False:
		org = p.IDENTITY_MARKET[returnRandomInt(0, len(p.IDENTITY_MARKET)-1)]
		if org.status == p.ACTIVE_1:
			found = True
	return org


def returnRandPerson():
	found = False
	while found == False:
		person = p.POPULATION[returnRandomInt(0, len(p.POPULATION)-1)]
		if person.status == p.ACTIVE_1:
			found = True
	return person

def already_account(person, org):
	match = False
	for accountID in person.accounts:
		account = p.ACCOUNTS[accountID]
		if account.orgID == org.orgID:
			match = True
	return match

def end_account(account):
	account.status = p.INACTIVE_0
	org = p.IDENTITY_MARKET[account.orgID]
	person = p.POPULATION[account.personID]
	org.users.remove(account.personID)
	person.accounts.remove(account.accountID)
	return 0


def make_friend(person):
	friend = get_unique_friend(person.personID, person.network)
	person.network.append(friend)
	person2 = p.POPULATION[friend]
	person2.network.append(person.personID) 
	return 0

def lose_friend(person, friendID):
	friend = p.POPULATION[friendID]
	#print "losing Friend/person", person.personID, friendID, person.network, friend.network
	person.network.remove(friend.personID)
	friend.network.remove(person.personID)
	
	return 0

