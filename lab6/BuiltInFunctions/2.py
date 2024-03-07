def measurement(str):
    sum = 0
    for i in range(len(str)):
        if str[i].isupper():
            sum += i
    return sum

str = str(input())
print(measurement(str))