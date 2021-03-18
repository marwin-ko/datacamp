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

  
  
# how to create a context manager (function implementation)
# 1. defin a function
# 2. (optional) add setup code
# 3. Use "yield" keyword
# 4. (optional) add teardown code
# 5. Add the '@contextlib.contextmanager' decorator

@contextlib.contextmanager
def my_context():
  # Add set up code
  yield
  # Add teardown code

