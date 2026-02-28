n, x = map(int, input().split())
arr = list(map(int, input().split()))

seen = {} 

for i in range(n):
    needed = x - arr[i]
    
    if needed in seen:
        print(seen[needed], i + 1)
        break
    
    seen[arr[i]] = i + 1
else:
    print("IMPOSSIBLE")