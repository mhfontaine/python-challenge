# import election data
import os
import csv

# working directory
# csvpath=os.path.join('..','Resources','election_data.csv')
election_data = os.path.join(r"/Users/marvinfontaine/Data-Analytics/Homework/python-challenge/PyPoll/Resources/election_data.csv")


# Variables
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Counting votes here 
        total_votes += 1 


        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Percentage of votes 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Winning candidate 
    winner = max(num_votes)
    index = num_votes.index(winner)
    win_can = candidates[index]

# Display election data results to the screen
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {win_can}")
print("--------------------------")

# Path to name and write output file
output_path = os.path.join("Analysis", "ElectionResultsFile.txt")

# Code to create output file
with open(output_path, 'w') as outfile:
     outfile.write("Election Results")
     outfile.write('\n')
     outfile.write("--------------------------")
     outfile.write('\n')
     outfile.write(str(f"Total Votes: {str(total_votes)}"))
     outfile.write('\n')
     outfile.write(str("--------------------------"))
     outfile.write('\n')
     for count in range(len(candidates)):
        outfile.write(f"{candidates[count]} {str(percent_votes[count])}% ({str(num_votes[count])}")
        outfile.write('\n')
     outfile.write("--------------------------")
     outfile.write('\n')
     outfile.write(f"Winner: {win_can}")
     outfile.write('\n')
     outfile.write("--------------------------")
outfile.close()
