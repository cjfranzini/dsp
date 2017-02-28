# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * `pwd` show current working directory path  
* `mkdir {dir}` create a directory
* `rmdir {dir}` delete a directory
* `touch {file}` create a file using `touch` command
* `rm {file}` delete a file
* `mv {file1} {file2}` rename a file by moving it to a new file with the desired name
* `ls -a` list all files, including hidden files
* `cp {filename} {dir}` copying a file from one directory to another
* `less {file}` view file by page
* `cat {file}` print contents of file in terminal

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > * `ls` list files in a directory
* `ls -a` list all files in a directory, including hidden files
* `ls -l` list files in a directory in long format
* `ls -lh` list files in a directory in long format and include unit suffixes
* `ls -lah` list all files in a directory, including hidden files, in long format and include unit suffixes
* `ls -t` list files in a directory sorted by time modified (most recent first)
* `ls -Glp` list files in a directory in long format, colorized, and with directories denoted with a trailing `/`

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -1` list files in a directory with one file per line
* `ls -R` list files in a directory and include subdirectories
* `ls -m` list files in a directory in comma-separated format
* `ls -r` list files in a directory in reverse alphabetical order
* `ls -C` list files in a directory in columnar format

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` performs the same command on a given list of inputs  
For example, `find *.txt | xargs rm` will find all text files within a directory and remove them

 

