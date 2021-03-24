# Context Manager

#
# analogy
#
# context manager      caterer
# set up a context     set up tables w/ food & drink
# run your code        you and your friends party
# remove the contet    clean up and remove tables 


# use cases
# open close DB
# change dir, do stuff, then change dir back
# open two files simulateously (nested context text mangagers)

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

# technically a generator that yields a single value
@contextlib.contextmanager
def my_context():
  # Add set up code
  yield
  # Add teardown code

  
# example 2 - database conn
@contextlib.contextmanager
def database(url):
  db = postgres.connect(url)
  yield db
  db.disconnect()
url = 'http://datacamp.com/data'
with database(url) as my_db:
  course_list = my_db.execute(
    'SELECT *
    FROM courses'
  )

  
# example 3 - timer
@contextlib.contextmanager
def timer():
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)
  
  
# 
# Advanced examples
# 

# example 4 - context manager with error handling
def in_dir(directory):
  """
  Change current working directory to `directory`,
  """
  current_dir = os.getcwd()
  os.chdir(directory)
  
  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)
    
    
# example 5 - open two "sources" with nested context manager
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

