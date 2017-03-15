[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

This exercised asks to use parameters of the BRFSS male height distribution to approximate the distribution of all U.S. male heights. It then asks to find out what portion of the U.S. male population falls within the range of heights required to join the Blue Man Group.

To solve this is used the scipy.stats library as the author suggests. I set the mean and standard deviation variables to the BRFSS parameters and used scipy.stats.norm to general a normal distribution with those parameters. I then converted the height range bounds from inches to cm because the BRFSS data is in cm and used scipy.stats.norm.cdf to compute the difference in cumulative probabilities for the upper and lower bounds to get the required proportion.

---
```python
import scipy.stats

# use the parameters of the BRFSS distribution of mens' heights
# to model distribution
mu = 178
sigma = 7.7

# general normal distribution using parameters
dist = scipy.stats.norm(loc=mu, scale=sigma)

# set and convert limits from inches to cm
upper_cm = 73 * 2.54
lower_cm = 70 * 2.54

# calculate difference in proportions for proabability of range
dist.cdf(upper_cm) - dist.cdf(lower_cm)
```

---
```python
0.34274683763147457
```

---
Using a normal distribution with the parameters of the BRFSS distribution of male heights estimates that approximately 34.28% of the U.S. male population meets the Blue Man Group height requirement. This is reasonable considering that the BRFSS mean male height is about 6'0" and the standard deviation is about 3". With the assumption that the distribution is normal, about 65% of the population would fall between 5'9" and 6'3", which is a range of 6". The Blue Man Group height requirement constitutes a subset range of 3" within the range of the mean plus or minus the standard deviation and 34% is roughly half of 65%.