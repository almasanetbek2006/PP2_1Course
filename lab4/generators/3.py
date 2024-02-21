import json

def square(N):
    for i in range(1, N+1):
        if i%3==0 and i%4==0:
            yield i

        
N = int(input())
aa = list(square(N))
print(json.dumps(aa))