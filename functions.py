# functions
def my_function(x,y,z = 1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
    
# lambda functions

def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2

# Currying

def add_numbers(x, y):
    return x + y
add_five = lambda y: add_numbers(5,y)
from functools import partial
add_five = partial(add_numbers, 5)

# generator
def squares(n=10):
    print('Generating squares from 1 to {0}' .format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2


# generator

def _make_gen():
    for x in range(100):
        yield x ** 2
    gen = _make_gen()


#exception handling

def attempt_float(x):
    try:
        return float(x)
    except:
        return x


