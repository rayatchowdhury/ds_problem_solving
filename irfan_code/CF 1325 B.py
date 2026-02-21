
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    unique = set(a)
    print(len(unique))