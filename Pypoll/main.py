import os
import csv
from typing import Counter

election_csv = os.path.join("C://Users//16692//Desktop//python-challange//Pypoll//resources//election_data.csv")
votes = []
# open and read csv
with open(election_csv)as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
 #skip the header row
    next(csv_reader)
    

    for row in csv_reader:
        votes.append(row[2]) # assuming candidate name is in the first column

#count votes
vote_counts = Counter(votes)
     

#Total number of votes cast
Total_votes = len(votes)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_votes}")
print("----------------------------")

#Complete List of candidates who recieved votes
results = []
for candidate,vote_count in vote_counts.items():
    percentage = (vote_count/Total_votes) *100
    results.append((candidate,vote_count,percentage))

#Determine winner
winner = max(results, key=lambda x: x[2])
winner_name = winner[0]  
    

#print results
print("Results:")
for candidate,vote_count,percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({vote_count})")
     


#print the winner outside the loop  
print("--------------------------")

print(f"Winner: {winner_name}")

print("---------------------")

#exporting the resuts to the text file.
with open("election_analysis.txt","w")as file:
    file.write("Election Results\n")
    file.write("---------------------\n")

    file.write(f"Total Votes: {Total_votes}\n")
    file.write("--------------------\n")

    file.write("Results\n")
    for candidate,vote_count,percentage in results:
        file.write(f"{candidate}: {percentage:.3f}% ({vote_count})\n")
    
    file.write("-------------------------------\n")

    file.write(f"Winner: {winner_name}\n")

    file.write("---------------------------")
