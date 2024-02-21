import json

def square(N):
    for i in range(0, N+1):
        if i%2==0:
            yield i
    
        
N = int(input())
aa = list(square(N))
print(json.dumps(aa, separators=(" ", " ")))