# Hint:  use Google to find python function

from datetime import datetime

def time_diff(start, stop, form):
    '''Takes a start time and stop time in a given string format and calculates the difference in days
    '''
    start_dt = datetime.strptime(start, form)
    stop_dt = datetime.strptime(stop, form)

    td = stop_dt - start_dt

    return td.days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

print time_diff(date_start, date_stop, '%m-%d-%Y')


####b)  
date_start = '12312013'  
date_stop = '05282015'  

print time_diff(date_start, date_stop, '%m%d%Y')

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

print time_diff(date_start, date_stop, '%d-%b-%Y')