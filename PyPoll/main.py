#importing modules 
import csv
import os
import statistics
#reading csvfile
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    #storing header row
    header = next(csvreader)
    #converting csvfile's data into list
    candidates_list = [] 
    for row in csvreader:
        candidate = row[2]
        candidates_list.append(candidate)
    #identifying candidates' names
    candidates_names = sorted(list(set(candidates_list)))
    #finding total number of vote counts
    vote_count = len(candidates_list)
    #calculating vote counts for each candidates
    Charles_vote=0
    Diana_vote=0
    Raymon_vote=0
    for name in candidates_list:
        if name == "Charles Casper Stockham":
            Charles_vote += 1
        elif name == "Diana DeGette":
            Diana_vote += 1
        elif name == "Raymon Anthony Doane":
            Raymon_vote += 1
    #calculating %vote counts of each candidates
    Charles_pct = Charles_vote/vote_count*100
    Diana_pct = Diana_vote/vote_count*100
    Raymon_pct = Raymon_vote/vote_count*100
    #finding the candidates with most the votes
    winner = statistics.mode(candidates_list)
#converting variables into string for printing 
election = f'''
    Election Results
    --------------------
    Total Votes: {vote_count}
    --------------------
    {candidates_names [0]}: {round(Charles_pct,3)}% ({Charles_vote})
    {candidates_names [1]}: {round(Diana_pct,3)}% ({Diana_vote})
    {candidates_names [2]}: {round(Raymon_pct,3)}% ({Raymon_vote})
    --------------------
    Winner: {winner}
    --------------------
    '''
#printing result of the election in terminal
print (election)
#creating new txtfile for exporting election results
new_path = os.path.join('Analysis','Election_Results.text')
with open(new_path,'w', newline ='') as txtfile:
    txtfile.write(election)