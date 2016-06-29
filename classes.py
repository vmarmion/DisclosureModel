#!/usr/bin/python

import parameters as p
import functions as f


"""------------------------------------------------------------------------------------------------------------------------------
---------------- 	CREATE CLASSES
----------------
----------------
---------------------------------------------------"""

class account_CLASS:

	def __init__(self, accountID):

		self.accountID = accountID
		self.orgID = 0
		self.marketID = 0
		self.personID = 0
		self.time = 0
		self.status = p.ACTIVE_1
		self.ID_disclosure = []


	def displayACCOUNT(self):
		
		AccountInfo = "Account ID:%s OrgID:%s PersonID:%s MarketID:%s Time%s Status:%s, Disclosure:%s" % (self.accountID, self.orgID, self.personID, self.marketID, self.time, self.status, self.ID_disclosure)

		
		return AccountInfo

class Organisation_CLASS:
	
	def __init__(self, orgID, marketID):
		self.orgID = orgID
		self.marketID = marketID
		self.REPUTATION = 0
		self.BANDWAGON = 0
		self.marketShare = 0
		self.revenue = 0
		self.initialInvestment = 0
		self.status = p.ACTIVE_1
		self.users = []
		self.strategy = 0
		self.IDRequest = []
		self.age = 0
		

	def displayORG(self):
		orgInfo = "OrgID:%s Type:%s Users:%s Age:%s EMU%s Strategy:%s ID_Request:%s, REPUTATION:%s" % (self.orgID, self.marketID, self.users, self.age, self.revenue, self.strategy, self.IDRequest, self.REPUTATION)

		
		return orgInfo

class Person_CLASS:

	def __init__(self, personID):
		self.personID = personID
		self.accounts = []
		self.network = []
		self.regulatoryFocus = f.returnRandomReal()
		self.availability = [0,0] 
		self.status = p.ACTIVE_1
		self.age = 5
				

	def displayPERSON(self):
		personInfo = "personID:%s Age:%s Network:%s Status:%s Accounts%s RegFocus:%.2f Availablity:%s" % (self.personID, self.age, self.network, self.status, self.accounts, self.regulatoryFocus, self.availability)

		return personInfo