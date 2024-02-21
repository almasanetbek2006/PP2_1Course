import math
def radian(degree):
    radians = degree * (math.pi / 180)
    return radians


degree = int(input("input degree: "))
aa = radian(degree)
print(aa)