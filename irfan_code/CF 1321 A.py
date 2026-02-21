n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))

onlyR = 0
onlyB = 0

for i in range(n):
    if r[i] == 1 and b[i] == 0:
        onlyR += 1
    elif r[i] == 0 and b[i] == 1:
        onlyB += 1

if onlyR == 0:
    print(-1)
else:
    ans = onlyB // onlyR + 1
    print(ans)