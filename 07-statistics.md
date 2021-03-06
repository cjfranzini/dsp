# Statistics

# Table of Contents

[1. Introduction](#section-a)  
[2. Why We Are Using Think Stats](#section-b)  
[3. Instructions for Cloning the Repo](#section-c)  
[4. Required Exercises](#section-d)  
[5. Optional Exercises](#section-e)  
[6. Recommended Reading](#section-f)  
[7. Resources](#section-g)

## <a name="section-a"></a>1.  Introduction

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)

Use Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) book for getting up to speed with core ideas in statistics and how to approach them programmatically. This book is available online, or you can buy a paper copy if you would like.

Use this book as a reference when answering the 6 required statistics questions below.  The Think Stats book is approximately 200 pages in length.  **It is recommended that you read the entire book, particularly if you are less familiar with introductory statistical concepts.**

Complete the following exercises along with the questions in this file. Some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

## <a name="section-b"></a>2.  Why We Are Using Think Stats 

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  **You could import it, or you could write your own code to practice python and develop a deeper understanding of the concept.** 

Think Stats uses a higher degree of python complexity from the python tutorials and introductions to python concepts, and that is intentional to prepare you for the bootcamp.  

---

## <a name="section-c"></a>3.  Instructions for Cloning the Repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/metisgh/prework  
(Windows):  C:/ds/metis/metisgh/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/metisgh/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/metisgh/prework/ThinkStats2/code
```

---


## <a name="section-d"></a>4.  Required Exercises

*Include your Python code, results and explanation (where applicable).*

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

### Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 



### Q5. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  
 

>> We want to know the probability Elvis is an identical twin given that he had a twin brother who died at birth. Put another way, we want to know the probability Elvis was an identical twin given that he was a twin. In this situation there are two hypotheses: Elvis was an identical twin and Elvis was a fraternal twin. We only care about the first but it will help to compute both. The hypotheses meet Downey's requirements of being both mututually exclusive and collectively exhaustive.    

>> This problem can be solved nicely using the table method described by Downey in chapter one of *Think Bayes*.   

>> The prior probability for each hypothesis (p(H)) is the stated probability observed in the population, so 1/300 for indentical twin and 1/125 for fraternal twin. The likelihood (p(D|H)) is the probability Elvis was a twin given that he was either an idential twin or a fraternal twin, which is one for both. That makes the product (p(H)p(D|H)) easy to compute. The normalizing constant (p(D)) is the sum of the two prior probabilities: 17/1500. Normalizing the products shows p(A|D) to be 5/17 and p(B|D) to be 12/17.

>> 
>> Hypothesis | p(H) | p(D&#124;H) | p(H)p(D&#124;H) | p(H&#124;D)
>> ------------ | ------------- | ------------ | ------------- | ------------
>> A | 1/300 | 1 | 1/300 | 5/17
>> B | 1/125 | 1 | 1/125 | 12/17

>> Therefore, for this particular population, the probability that Elvis was an identical twin given that he had a twin brother is 5/17.


---

### Q6. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>> Frequentist and Bayesian statistics seem to me two different perspectives rather than disparate fields of statistics. In fact, I think treating them as wholly different has made it more difficult for me to understand their differences because I'm not convinced one is better than the other. Nor am I convinced that one should be used exclusively instead of the other. I think it depends on what you want to know. The main difference between the two lies in the definition of probability. Frequentists consider probability an expression of frequency. That is, if a frequentist says the probability of an event is 60% what is meant is that if an observation is made ten times the event will be observed six times. On the other hand, if a Bayesian says the probability of an event is 60% what is meant is that the Bayesian is 60% certain the event will be observed.  

>>In practice, frequentist statistics assert that populations have 'true' parameters that can be approximated from the descriptive statistics of many independent samples of the population. Bayesian statistics rejects the idea that there is any singular truth about a population and instead asserts that the parameter of a population can be any one of a range of values each with its own likelihood. Both allow for either informed or uninformed prior assumptions to affect analysis. In Bayesian statistics it is necessary. In frequentist it is not but it is reasonable to imagine a situation where you might do so. For instance, income distributions are rarely linear so it would be reasonable to make a prior assumption about the non-linearity of a relationship involving income data. Both also depend on repeated observations to improve upon prior assumptions.  

>> Both types of analysis acknowledge uncertainty as the outcome of each is expressed as a range of values. The result of a Bayesian analysis is a range of values each with its own likelihood. The result of a frequentist analysis is a range of values and the likelihood, expressed as the confidence interval, is the expected frequency with which the 'truth' occurs within the range. 

---

## <a name="section-e"></a>5.  Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

### Q7. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

### Q8. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

### Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
### Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
### Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

---

## <a name="section-f"></a>6.  Recommended Reading

Read Allen Downey's [Think Bayes](http://greenteapress.com/thinkbayes/) book.  It is available online for free, or you can buy a paper copy if you would like.

[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/) 

---

## <a name="section-g"></a>7.  More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.
