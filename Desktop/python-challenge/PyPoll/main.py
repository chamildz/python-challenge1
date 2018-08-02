import csv
import os
import operator

csv_file_path = os.path.join("Resources","election_data.csv")

#Declare the variable to store the number of rows
row_count=0

#Initializes an empty dictionary which will be used to store election stats
electionStatsDictionary = dict()

#Uses electionSummaryResultsString to build final election summary message
electionSummaryResultsString = "Election Results \n"
electionSummaryResultsString += "-----------------------\n"

with open(csv_file_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvfile)
    
    for row in csvreader:
        row_count+=1
        candidateName=row[2]
        if candidateName in electionStatsDictionary:
            electionStatsDictionary[candidateName]+=1
        else:
            electionStatsDictionary[candidateName]=1

electionSummaryResultsString+=f"Total Votes: {row_count}\n"
electionSummaryResultsString +=f"----------------------------\n"

for (k,v) in electionStatsDictionary.items():
    votePercent = round(v*100/row_count,3)
    electionSummaryResultsString+=f"{k} : {votePercent}% ({v})\n"

electionSummaryResultsString +=f"----------------------------\n"

#finding the key which is  having maximum value
winner = max(electionStatsDictionary.items(),key=operator.itemgetter(1))[0]

electionSummaryResultsString+=f"Winner : {winner} \n"
print(electionSummaryResultsString)


    
            
        

