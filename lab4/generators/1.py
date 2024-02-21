import json

def square(N):
   # result = list(i**2 for i in range(1, N+1))
   # return json.dumps(result, separators=(" ", " "))
    for i in range(1,N+1):
        yield i**2
        
N = int(input())
aa = list(square(N))
print(json.dumps(aa, separators=(" ", " ")))