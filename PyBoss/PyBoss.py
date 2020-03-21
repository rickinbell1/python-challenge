import os
import csv
name,name1,emp =[],[],[]
FirstName,LastName = [], []
date_birth,md_y = [], []
ssn,ssn_N = [], []
new_st =[]
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

csvpath = os.path.join("..","BootCamp_Data","USC-LA-DATA-PT-08-2019-U-C","03-Python","Homework","Instructions","ExtraContent","Instructions","PyBoss","employee_data.csv")
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        emp.append(row[0])
        name.append(row[1])
        date_birth.append(row[2])
        ssn.append(row[3])
        new_st.append(row[4])
    for i in range(len(name)):
        name1.append(name[i].split())
    LastName = [i[1] for i in name1] 
    FirstName = [i[0] for i in name1] 
    for i in range(len(date_birth)):
        md_y.append(date_birth[i][5:7] +"/"+date_birth[i][8:]+"/"+date_birth[i][0:4])
    for i in range(len(ssn)):
        ssn_N.append(ssn[i].replace(ssn[i][0:6],"***-**"))
    for i in range(len(new_st)):
        if new_st[i] in us_state_abbrev:
            new_st[i] = us_state_abbrev[new_st[i]]
            
filepath = os.path.join("..","employ_data.csv")
with open(filepath,'w',newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["EMP ID","First Name","Last Name","DOB","SSN","State"])
    for i in range(len(emp)):
        csv_writer.writerow([emp[i],FirstName[i],LastName[i],md_y[i],ssn_N[i],new_st[i]])