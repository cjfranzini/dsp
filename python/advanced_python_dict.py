### 05b-python_advanced.md Q6, Q7, and Q8 ###

### Q6 ###

import csv
import string

def faculty_last_name_dict():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a dictionary of the  faculty grouped by last name
    '''
    
    with open('faculty.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        faculty_dict = {}
        
        for row in reader:
            name = row['name']
            last_name = name.split()[-1]
            degree = row[' degree'].strip()
            email = row[' email'].strip()
            title = row[' title'].strip()
            
            # filter out 'of Biostatistics' in titles
            prof_i = title.lower().find('professor')
            title = title[:(prof_i + len('professor'))]
            
            entry = [degree, title, email]
            
            if last_name not in faculty_dict.keys():
                faculty_dict[last_name] = []
            
            out = faculty_dict[last_name]
            out.append(entry)
            
            faculty_dict[last_name] = out
            
    return faculty_dict 
        
print faculty_last_name_dict()



### Q7 ###

def faculty_first_last_dict():
    '''Reads a csv file of the Biostats Faculty at the University of Pennsylvania and generates a dictionary of the  faculty grouped by (first name, last name) tuples
    '''
    
    with open('faculty.csv', 'r') as f:
        reader = csv.DictReader(f)
        
        faculty_dict = {}
        
        for row in reader:
            name = row['name']
            last_name = name.split()[-1]
            first_name = name[:name.find(last_name)].strip()
            
            degree = row[' degree'].strip()
            email = row[' email'].strip()
            title = row[' title'].strip()
            
            # filter out 'of Biostatistics' in titles
            prof_i = title.lower().find('professor')
            title = title[:(prof_i + len('professor'))]
            
            entry = [degree, title, email]
            
            if (first_name, last_name) not in faculty_dict.keys():
                faculty_dict[(first_name, last_name)] = entry
            
    return faculty_dict 
        
print faculty_first_last_dict()



### Q8 ###

def faculty_fl_dict_sorted():
    '''Sorts the dictionary of UPenn Biostats faculty created calling faculty_first_last_dict() by last name and returns the sorted dictionary
     '''
    
    faculty_dict = faculty_first_last_dict()
    keys = faculty_dict.keys()
    rev_keys = []
    for key in keys:
        rev_keys.append(key[::-1]) # reverse keys to be (last_name, first_name)
    
    sorted_keys = sorted(rev_keys) # sort by last name

    for s in sorted_keys:
        print str(s[::-1]) + ': ' + str(faculty_dict[s[::-1]])
        
    
faculty_fl_dict_sorted()    
