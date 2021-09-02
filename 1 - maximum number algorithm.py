""" 
Design an algorithm that finds the maximum positive integer input by a user.  
The user repeatedly inputs numbers until a negative value is entered.
 
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.
 
During the design of your algorithm and your implementation, you should use git:
Initialize a local directory with git init.
Write the text of your algorithm in a file called max_int.py
Inspect the result of git status
Use git add . to move changes to the staging area.
Commit your changes with git commit -m “Algorithm written for max_int”
Then start implementing your algorithm
During your implementation, make sure you do git status, git add, and git commit regularly.
You can see a log of all your commits with git log.
When you have finished your implementation:
Create an account on github.com (if you don't already have it).
Create a public repository on github
Follow the instructions (that appear on github when you have created a new repository) under 
"push an existing repository from the command line"  (see also here)
Push your changes to the remote repo with: git push
Inspect your commits on github 
"""

# Algorithm
# 1 - ask user for number
# 2 - ask user for another number
# 3 - compare the two numbers
# 4 - store the higher number
# 5 - ask user for another number
# 6 - compare the new number to the stored number
# 7 - store the higher number
# 8 - ask user again until the user inputs a negative number
# 9 - then print out the highest number.


num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

print("The maximum is", max_int)    # Do not change this line
