# -*- coding: UTF-8 -*-
# Import modules
import os
import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create path to .csv datafile
filepath = os.path.join("Resources", "employee_data.csv")

# Define variables and lists
first_name = []
last_name = []
date_reformat = []
ssn_list = []
abbrev_state = []
employee_id = []
new_employee_dict = {}

# first=fullname.split()[0]
# last=fullname.split()[-1]
# print(first + ',' + last)

def new_date(date):
    year = date.split("-")[0]
    month = date.split("-")[1]
    day = date.split("-")[2]
    new_date_string = str(month + "/" + day  + "/" + year)
    return new_date_string

def SSN_rework(ssn):
    return str("***-**-" + ssn.split("-")[2])

# Open .csv datafile
with open(filepath) as csvfile:
    # Use csv module with reader module to read file / delimited by commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Skip header row
    csv_header = next(csvreader)
    for row in csvreader:
        first_name.append(row[1].split()[0])
        last_name.append(row[1].split()[1])
        date_reformat.append(new_date(row[2]))
        ssn_list.append(SSN_rework(row[3]))
        abbrev_state.append(us_state_abbrev[row[4]])
        employee_id.append(row[0])

new_employee_file = zip(employee_id, first_name, last_name, date_reformat, ssn_list,abbrev_state)

# Set variable for output file
output_file = os.path.join("Output", "new_employee_data.csv")
#  Open the output file
with open(output_file, "w", newline = "\n") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    # Write in zipped rows
    writer.writerows(new_employee_file)




    

        





