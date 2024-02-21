import math
def polygon(s, l):
    area = (s * (l**2))/(4*math.tan(math.pi / s))
    return area
s, l = map(int,input("sides, length").split(" "))
aa=polygon(s, l)
print(f"Expected Output: {aa}")