# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Import csv module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Create variables and set initial values
total_months = 0
net_PandL = 0
sum_change = 0
profit_previous_row = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # Add 1 to total_months as script iterates through each row to count months
        total_months = total_months + 1
        # Sum the profit and loss column to get to net proft
        net_PandL = net_PandL + int(row[1])
        # Ignore first row because change calc not valid
        if total_months > 1:
            # Calculate profit change and add to running total
            sum_change = sum_change + int(row[1]) - profit_previous_row
            # Update greatest_increase variables if current profit > previous greatest
            if int(row[1]) > greatest_increase:
                greatest_increase = int(row[1]) - profit_previous_row
                greatest_increase_month = row[0]
            else: 
                pass
             # Update greatest_decrease variables if current profit > previous greatest
            if int(row[1]) < greatest_decrease:
                greatest_decrease = int(row[1]) - profit_previous_row
                greatest_decrease_month = row[0]
            else: 
                pass
        else:
            pass    
        # Update profit or loss for change calculation
        profit_previous_row = int(row[1])

    # Print out results
    print("Financial Analysis")
    print("----------------------------")
    print("Total months: " + str(total_months))
    print("Total net profit: " + str(net_PandL))
    print("Average profit change: " + str(sum_change/(total_months - 1)))
    print("Greatest monthly profit: " + str(greatest_increase_month) + "(" + str(greatest_increase) + ")")
    print("Greatest monthly loss: " + str(greatest_decrease_month) + "(" + str(greatest_decrease) + ")")

# Export results to .txt file

output_path = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Item', 'Value'])

    # Write the second row
    csvwriter.writerow(['Total months: ', str(total_months)])

