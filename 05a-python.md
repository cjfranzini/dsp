# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they are both data structures and types of sequences. They also resemble each other syntactically as values separated by commas, but a list is enclosed in brackets while a tuple is often enclosed in parenthesis but does not need to be. The most significant difference between lists and tuples is that lists are mutable and tuples are immutable. The keys of a dictionary must be immutable and therefore a tuple can be used as a dictionary key but a list cannot. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both mutable collections of objects, but lists are indexed and sets are not. Syntactically lists and sets are both values separated by commas but lists are enclosed with brackets and sets are enclosed with braces. In the first example below, it makes sense to use a list for elements that have some inherent order, such as the days of the week. In the second example, a set can be used for colors because there is no particular order to colors and so the position of each element in the set is not significant.  

>> `# example of list`  
    `days = ['Monday','Tuesday','Wednesday','Thursday','Friday']`

>> `# example of set`  
    `colors = {'red','blue','green','yellow','purple'}`
    
>> For large collections, sets are faster for finding an element than lists. The reason is that the elements of a set are required to be hashable while lists are inherently unhashable. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a Python construct that allows for the creation of anonymous functions, which do not need to be defined or assigned to a variable. These functions are useful in instances when a fully-defined function is unnecessary. `lambda` functions always return a value or object and are forgotten unless assigned to a variable.  

>> The following example uses a lambda function in the `key` parameter for `sorted` to deal with the discrepancies in capitalization among the list items. The function calls lower on each item in the list in order to sort the items by their lowercase form.

>> `# example of using lambda with sorted`      
    `cities = ['New york', 'boston', Chicago', 'los Angeles']`  
    `sorted(cities)`  
    `>> ['Chicago', 'New york', 'boston', 'los Angeles']`  
    `sorted(cities, key = lambda x: x.lower())`  
    `>> ['boston', 'Chicago', 'los Angeles', 'New york']`

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Python list comprehensions allow for the succinct construction of lists. For instance, as the following example shows, a list can be constructed using a loop in only a couple of lines of code but using a list comprehension the same list can be constructed in only one line of code.  

>> ```python
    # using loop 
    x = []  
    for n in range(1,6):  
        x.append(n**2)   
```  
>> ```python  
    # using list comprehension
    x = [n**2 for n in range(1,6)]
```  
>> The above list can also be constructed using `map` if `n` is already defined.  
>> ```python
    n = range(1,6)  
    x = map(lambda y: y**2, n)  
```  
>> Again, the list comprehension is more succinct.  
    
>> A list comprehension can also be used in place of `filter`.  
>> ```python  
    # using filter
    n = range(1,10)  
    y = filter(lambda x: x % 3 == 0, n)
```  
>> ```python  
    # using list comprehension
    y = [x for x in range(1,10) if x % 3 == 0]  
```  
>> A list comprehension can replace `map` or `filter` in instances when `for` or `if` statements are all that is required to construct the list. For anything more complicated `map` or `filter` should be used. A list comprehension should also not be used when the argument for constructing the list changes in time.  

>> A set comprehension is constructed similarly to a list comprehension except that it is bounded by braces.  
>> ```python
    s = {float(x) / (x**2) for x in range(1,10)}  
```  
    
>> The same set can be constructed using a dictionary comprehension with initial values of `x` as the keys.  
>> ```python
    d = {x: float(x) / (x**2) for x in range(1,10)}  
```


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





