[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

---

This problem asks to use Cohen's d to quantify the effect size between the distributions of weight (lb) for first-birth babies and all other babies (second, third, fourth, etc.). The problem then asks to do the same with the pregnancy length distributions for the two groups.  

Cohen's d measures effect size between two groups by calculating the difference between the mean of each group and then standardizing the mean difference by the standard deviation of the two distributions combined. Discussing effect size in terms of a proportion of the combined standard deviation is more straightforward than doing so in terms of the original units.  

To solve this problem, I first loaded in the necessary python libraries and the dataset. I then selected the subset of live births since I was not interested in the alternatives. Next I split the data into two groups--first births and other births--using the 'birthord' (birth order) variable. Finally, I called the author's CohenEffectSize function on the 'totalwgt_lb' and 'prglngth' series of each group. 

My code is largely based off of the author's code in Chapter 2. 

---


```python  
"""use author's provided code to import libraries and read in 
pregnancy data
"""

%matplotlib inline

import numpy as np

import nsfg
import first

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1] # select only live births

# group live births by first pregnancy and all others using 'birthord'
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# author's function to compute Cohen's d
def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.
    
    group1: Series or DataFrame
    group2: Series or DataFrame
    
    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

# call CohenEffectSize on 'totalwgt_lb'
total_wgt_d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

# call CohenEffectSize on 'prglngth'
prglngth_d = CohenEffectSize(firsts.prglngth, others.prglngth)

print 'Total Weight Effect Size: ' + total_wgt_d
print 'Pregnancy Length Effect Size: ' + prglngth_d

```
---
```python  
Total Weight Effect Size: -0.0886729270726
Pregnancy Length Effect Size: 0.0288790446544
```
---
Cohen's d for 'totalwgt_lb' between first births and other births is approximately -0.089, which tells me first-birth babies tend to be lighter than other-birth babies but by less than 1% of the combined standard deviation. Cohen's d for pregnancy length is about 0.029, so first-birth pregnancies tend to last longer than other-birth pregnancies but not by much. The effect size of total weight is about three times as much as that for pregnancy length.
