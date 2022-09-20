from functools import reduce

def triangular(x):
    return reduce(lambda x,y: x+y , range(1,x+1))

print(triangular(5))
