# Context Manager

#
# analogy
#
# context manager      caterer
# set up a context     set up tables w/ food & drink
# run your code        you and your friends party
# remove the contet    clean up and remove tables 


# format
with <context-manager>(<args>) as <variable-name>:
  # run code
  # this code is running "inside the context"


# example 1
with open('testfile.txt') as file:
  text = file.read()
