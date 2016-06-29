rm(list = ls(all = TRUE))
setwd("~/Dropbox/PhD_identity/CH7_Disclosure_Model/Ex7_Identity_Exposure/OutputFiles")
datafilenameORG = "ORG_ _P100_Y10_S10_outputfile.csv"
datafilenameACC = "ACC_ _P100_Y10_S10_outputfile.csv"
datafilenameUSER = "USER_ _P100_Y10_S10_outputfile.csv"
data.factorsORG = read.csv(datafilenameORG,header=TRUE, row.names = 1) 
data.factorsACC = read.csv(datafilenameACC,header=TRUE, row.names = 1) 
data.factorsUSER = read.csv(datafilenameUSER,header=TRUE, row.names = 1) 

summary(data.factorsORG)
summary(data.factorsACC)
summary(data.factorsUSER)
