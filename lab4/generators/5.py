import json

def square(N):
    for i in range(0, N+1):
            yield i

        
N = int(input())
aa = list(square(N))
bb = aa[::-1]
print(json.dumps(bb))