# -*- coding: UTF-8 -*-
# Import modules
import os
import csv

# Create path to .csv datafile
filepath = os.path.join("Resources", "election_data.csv")

# Define variables and lists
a = 0
b = 0
candidate_list = []
votes_tally = []
votes_percentages = []

# Open .csv datafile
with open(filepath) as csvfile:
    # Use csv module with reader module to read file / delimited by commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip header row
    csv_header = next(csvreader)
    # Create a loop to read each row of .csv datafile
    for row in csvreader:
        # Remove duplicate candidate names, by
        # Create an if statement to add (append) a new 
        # (i.e. not in current list) candidate name to list 
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            # Add (append) a zero placeholder in the votes 
            # tally list for each new candidate
            votes_tally.append(0)
        # Add a vote to the corresponding candidate
        # Loop through candidate list / corresponding index (i)
        for i, candidate in enumerate(candidate_list):
            # Once candidate identified..
            if candidate == row[2]:
                # Update current vote tally by one for that candidate
                a = int(votes_tally[i])
                votes_tally[i] = a + 1
            # Or do nothing!
            else:
                pass

# Define a function to calculate the % of votes and format to 3 decimal places
def calculate_percent(votes):
    return "{0:.3%}".format(votes/sum(votes_tally))

# Add % of votes to new list at appropriate index
for j, candidate in enumerate(candidate_list):
    b = calculate_percent(votes_tally[j])
    votes_percentages.append(b)

# Winner is candidate with most votes!
Winner = candidate_list[votes_tally.index(max(votes_tally))]

# Print results to terminal
c = ""
d = ""
e = ""

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(sum(votes_tally)))
print("-------------------------")
for k in range(len(candidate_list)):
    c = str(candidate_list[k])
    d = str(votes_percentages[k])
    e = str(votes_tally[k])
    print(c + ": " + d + " (" + e + ")")
print("-------------------------")
print("Winner: " + str(Winner))
print("-------------------------")

# Export results to .txt file

output_path = os.path.join("Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = "\n") as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')
    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Votes: " + str(sum(votes_tally))])
    csvwriter.writerow(["-------------------------"])
    for k in range(len(candidate_list)):
        c = str(candidate_list[k])
        d = str(votes_percentages[k])
        e = str(votes_tally[k])
        csvwriter.writerow([c + ": " + d + " (" + e + ")"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Winner: " + str(Winner)])
    csvwriter.writerow(["-------------------------"])

