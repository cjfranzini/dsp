### Q5 ###

import csv

def emails_csv():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and writes a list of the faculty email addresses to a new csv file (emails.csv)
    '''
    
    with open('faculty.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        email_list = []
      
        for row in reader:
            if row[' email'] not in email_list: # check for duplicates
                email_list.append(row[' email'])
    
    with open('emails.csv', 'w') as out:
        writer = csv.writer(out, delimiter = '\n')
        writer.writerow([email for email in email_list])

emails_csv()