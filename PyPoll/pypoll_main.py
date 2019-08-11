import os
import csv

pyelec_csv = os.path.join("Resources", "election_data.csv")

voter_id=[]
county=[]
candidate=[]

with open(pyelec_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) 
    
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
total_votes=len(voter_id)

candidates_list=[]

new_data_set=zip(voter_id,candidate)
li_votes=0
otooley_votes=0
khan_votes=0
correy_votes=0
for row in new_data_set:
    if row[1] not in candidates_list:
        candidates_list.append(row[1])
    if row[1]=="Li":
        li_votes=li_votes+1
    elif row[1]=="O'Tooley":
        otooley_votes=otooley_votes+1
    elif row[1]=="Khan":
        khan_votes=khan_votes+1
    else:
        correy_votes=correy_votes+1
        
khan_votes_per=(khan_votes/total_votes)*100
rounded_khan=round(khan_votes_per,2)

correy_votes_per=(correy_votes/total_votes)*100
rounded_correy=round(correy_votes_per,2)

otooley_votes_per=(otooley_votes/total_votes)*100
rounded_otooley=round(otooley_votes_per,2)

li_votes_per=(li_votes/total_votes)*100
rounded_li=round(li_votes_per,2)

percentage_list=[rounded_li, rounded_otooley, rounded_khan, rounded_correy]        
votes_list=[khan_votes, correy_votes, li_votes, otooley_votes] 
results=zip(candidates_list, percentage_list, votes_list)
winner=[]
for row in results:
    if row[2]==max(votes_list):
        winner=row[0]

output=("Election Results"+"\n"+
        "-----------------"+"\n"+
        "Total Votes: "+ str(total_votes)+"\n"+
        "-----------------"+"\n"+
        "Khan: "+ str(rounded_khan)+"% "+ (str(khan_votes)) +"\n"+
        "Correy: "+ str(rounded_correy)+"% "+ (str(correy_votes))+"\n"+
        "Li: "+ str(rounded_li)+"% "+ (str(li_votes))+"\n"+
        "O'Tooley: "+ str(rounded_otooley)+"% "+ (str(otooley_votes))+"\n"+
        "-----------------"+"\n"+
        "Winner: "+ str(winner)+ "\n"+
        "-----------------"+ "\n")

print(output)

output_file = os.path.join("vote_report.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write(output)
