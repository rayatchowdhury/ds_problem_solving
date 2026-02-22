n = int(input())

e = []

for _ in range(n):
    a, b = map(int, input().split())
    e.append((a, 1))   
    e.append((b, -1))  

e.sort()

cu= 0
m = 0

for t, c in e:
    cu += c
    m = max(m, cu)

print(m)