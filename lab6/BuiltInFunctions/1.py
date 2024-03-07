import operator
import functools
def multi(list):
   result = functools.reduce(operator.mul,list)
   return result

list = [7,2,6,6]
print(multi(list))
