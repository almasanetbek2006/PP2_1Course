import math
def  parallelogram(l, h):
    area = l*h
    return area
l, h = map(int,input("length, height").split(" "))
aa= parallelogram(l, h)
print(f"Expected Output: {aa}")