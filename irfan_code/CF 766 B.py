n = int(input())
arr = list(map(int, input().split()))

arr.sort()

possible = False

for i in range(n - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        possible = True
        break

if possible:
    print("YES")
else:
    print("NO")
