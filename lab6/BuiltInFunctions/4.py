def squareroot():
    import time
    import math
    x = int(input("Input the value: "))
    y = int(input("Input the miliseconds: "))
    y=y/1000
    time.sleep(y)
    return f"Square root of {x} after {y} miliseconds is {math.sqrt(x)}"