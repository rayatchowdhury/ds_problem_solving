t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    used = set()
    count = 0
    
    for x in arr:
        if x not in used:
            used.add(x)
            count += 1
        elif x + 1 not in used:
            used.add(x + 1)
            count += 1
    
    print(count) 
    