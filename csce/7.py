n = int(input())
arr = list(map(int, input().split()))

c = arr[0]
ma = arr[0]

for i in range(1, n):
    c = max(arr[i], c + arr[i])
    ma = max(ma, c)

print(ma)