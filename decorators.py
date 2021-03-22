# Decorators


# SCOPE
# Scopes local (child function) >> nonlocal (parent function) >> Global >> Builtin
# keywords
# global, nonlocal


# CLOSURE
# Closure: a tuple of varaiables that are no loonger in scope, but that a functions needs in order to run.
# how to access closures
def funct():
  x=5
  def funct2():
    print(x)
  return bar


print(type(func.__closure__))
print(len(func.__closure__))
print(func.__closure__[0].cell_contents)
