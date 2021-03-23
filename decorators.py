# Decorators


# SCOPE
# Scopes local (child function) >> nonlocal (parent function) >> Global >> Builtin
# keywords
# global, nonlocal
# nonlocal variables: variables defined in the parent function that are used in the child function.


# CLOSURE
# Closure: a tuple of varaiables that are no loonger in scope, but that a functions needs in order to run.
# Closure: Nonlocal variables attached to a returned function 
def funct():
  x=5
  def funct2():
    print(x)
  return bar

# how to access closures
print(type(func.__closure__))
print(len(func.__closure__))
print(func.__closure__[0].cell_contents)

