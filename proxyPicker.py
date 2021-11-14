#   Date: 11/19/2021
#   Purpose: Select 5 random entries from csv; add them to a file to copy and paste into proxychain config file
#   Inputs: 
#        None
#   Outputs: 
#        Output is the text to copy-paste into proxy-chain.conf 
import csv
import random


ip = []
type = []
with open('proxyChain.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
                ip.append(row[0])
                type.append(row[1])
csvDataFile.close()

x = 3
while x > 0 :
    uniqueNumber = random.randrange(1,501)
    lineIP = ip[uniqueNumber]
    lineType = type[uniqueNumber]
    portIndex = lineIP.find(":")
    #print("Line IP: ", lineIP)
    linePort = lineIP[portIndex+1:]
    lineIP = lineIP[:portIndex]  
    print(f'{lineType:<10s} {lineIP:<20s} {linePort:<20s}')
    # print(lineType, "\t", lineIP, "\t", linePort)
    x = x -1

#print(ip)
#print(type)        