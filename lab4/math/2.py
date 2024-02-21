import math
def trapezoid(h,f,s):
    area = ((f+s)*h)/2
    return area
h,f,s = map(int,input("Height, first value, second value:").split(" "))
aa= trapezoid(h,f,s)
print(f"Expected Output: {aa}")