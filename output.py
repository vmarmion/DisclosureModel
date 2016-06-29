
"""
what to output?

Per market	
	Total number of orgs per year
	market latency per year

	Total number of accounts per year

	total Pbd/Growth strategy per year

	hist of org sizes throughout time
	hist of org ages throughout time
	hist of account time throughout time

	total value of identiy disclosed per year

	total market reputation per year
	
"""

import parameters as p
import csv

def writeCSV():

	with open("OutputFiles/ORG_ _P"+str(p.NUM_POPULATION)+"_Y"+str(p.YEARS)+"_S"+str(p.STEPS)+"_"+'outputfile.csv', 'w') as pOut:
		piiWriter = csv.writer(pOut, delimiter=',')
		header = "ORG_ID","TYPE","AGE","REPUTATION","NUM_USERS","STRATEGY"
		piiWriter.writerow(header)
		
		for org in p.IDENTITY_MARKET:
			row = org.orgID, org.marketID, org.age, org.REPUTATION, len(org.users), org.strategy
			piiWriter.writerow(row)
	pOut.close()

	with open("OutputFiles/USER_ _P"+str(p.NUM_POPULATION)+"_Y"+str(p.YEARS)+"_S"+str(p.STEPS)+"_"+'outputfile.csv', 'w') as pOut:
		piiWriter = csv.writer(pOut, delimiter=',')
		header = "PERSON_ID","AGE","NETWORK","STATUS","ACCOUNTS","REG_FOCUS","AVAILABILITY"
		piiWriter.writerow(header)
		
		for person in p.POPULATION:
			row = person.personID, person.age, len(person.network), person.status, len(person.accounts), person.regulatoryFocus, person.availability
			piiWriter.writerow(row)
	pOut.close()

	with open("OutputFiles/ACC_ _P"+str(p.NUM_POPULATION)+"_Y"+str(p.YEARS)+"_S"+str(p.STEPS)+"_"+'outputfile.csv', 'w') as pOut:
		piiWriter = csv.writer(pOut, delimiter=',')
		header = "ACC_ID","ORG_ID","PERSON_ID","MARKET","TIME","STATUS"
		piiWriter.writerow(header)
		
		for account in p.ACCOUNTS:
			row = account.accountID, account.orgID, account.personID, account.marketID, account.time, account.status
			piiWriter.writerow(row)
	pOut.close()
	return 0
