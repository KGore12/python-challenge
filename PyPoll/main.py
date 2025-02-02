#Data_Import
import os
import csv

#Declare your variables and values
total_votes_cast = 0
khan_votes = 0 
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Specify your path for the csv file from Resources file
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Open your CSV file
with open(csvpath, 'r') as csvfile:

    # Delimit the file using the comman & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read your header row first
    csv_header = next(csvfile)

    # read each row of data that is after the header
    for row in csvreader:
        
        # Calculate the total number of votes cast. 
        total_votes_cast += 1
        
        #Total Number Of Votes Each Candidate Won - calculation
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            

    #Percentage Of Votes Each Candidate Won - calculation
    kahn_percent = khan_votes / total_votes_cast
    correy_percent = correy_votes / total_votes_cast
    li_percent = li_votes / total_votes_cast
    otooley_percent = otooley_votes / total_votes_cast
    
    #Winner Of The Election Based On Popular Vote - calculation
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

#Print breakdown Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes_cast}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")



#File To Write To - Specification
output_file = os.path.join('..', 'PyPoll', 'Resources', 'election_data_outcome.text')

#Variables - Opening the File in "Write" Mode
with open(output_file, 'w',) as txtfile:

#New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes_cast}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
