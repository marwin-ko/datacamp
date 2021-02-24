def function(arg1, arg2=42):
  """
  Description of what the function does.
  
  Parameters
  ----------
  arg1 : type
    Description of arg1.
  arg2 : int, optional
    Write optional when an argument has a default value.
    Default=42.
    
  Returns
  -------
  The type of the return value
    Can include a description of the return value.
    Replace "Returns" with "Yields" if this function is a generator.
  """
  return arg1 + arg2



#
# Retrieving docstrings
#

# EXAMPLE 1
print(function.__doc__)

# EXAMPLE 2
import inspect
print(inspect.getdoc(the_answer))
