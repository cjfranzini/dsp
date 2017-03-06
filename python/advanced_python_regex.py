### Q1 ###
import csv
import string

def degree_hist():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a histogram of the degrees held by the faculty
    '''
    
    with open('faculty.csv') as f:
        reader = csv.DictReader(f)
        
        degree_dict = {}
#        counter = 0 # for sanity check
#        
        for row in reader:
            entries = row[' degree']
            
            for entry in entries.split():
#                counter += 1 # for sanity check
                entry = entry.strip()
                entry = entry.replace('.',' ') # address '.' discrepancy in degree titles
                out = string.join(entry.split(), '')
                out = out.lower()

                degree_dict[out] = degree_dict.get(out, 0) + 1

#    # sanity check                
#    dict_sum = 0
#    for val in degree_dict.values():
#        dict_sum += int(val)
#    
#    if counter == dict_sum:
#        print '%s = %s' % (counter, dict_sum)
#        print True
        
    return degree_dict  
        
print degree_hist()        
        

### Q2 ###

def title_hist():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a histogram of the titles held by the faculty
    '''
    
    with open('faculty.csv') as f:
        reader = csv.DictReader(f)
        
        title_dict = {}
#        counter = 0 # for sanity check
#        
        for row in reader:
            entry = row[' title']
            entry = entry.split()
            out = entry[0].strip()
            
#            counter += 1 # for sanity check

            title_dict[out] = title_dict.get(out, 0) + 1

#    # sanity check                
#    dict_sum = 0
#    for val in title_dict.values():
#        dict_sum += int(val)
#    
#    if counter == dict_sum:
#        print '%s = %s' % (counter, dict_sum)
#        print True
        
    return title_dict  
        
print title_hist()   


### Q3 ###

def list_emails():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a list of the faculty email addresses
    '''
    
    with open('faculty.csv') as f:
        reader = csv.DictReader(f)
        
        email_list = []
#        counter = 0 # for sanity check
#        
        for row in reader:
            if row[' email'] not in email_list: # check for duplicates
                email_list.append(row[' email'])
            
#                counter += 1 # for sanity check

#    # sanity check                
#    list_sum = len(email_list)
#    
#    if counter == list_sum:
#        print '%s = %s' % (counter, list_sum)
#        print True
        
    return email_list  
        
print list_emails()   


### Q4 ###

def unique_domains():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a list of the unique domains used for faculty email addresses
    '''
    
    with open('faculty.csv') as f:
        reader = csv.DictReader(f)
        
        domain_list = []
#        counter = 0 # for sanity check
        
        for row in reader:
            entry = row[' email']
            domain = entry.split('@')[1]
            domain = domain.strip()
            if domain not in domain_list: # check for duplicates
                domain_list.append(domain)
            
#                counter += 1 # for sanity check

#    # sanity check                
#    list_sum = len(domain_list)
#    
#    if counter == list_sum:
#        print '%s = %s' % (counter, list_sum)
#        print True
        
    return domain_list  
        
print unique_domains()