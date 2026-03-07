arr = list(map(int, input().split()))
n, k = map(int, input().split())
queries = list(map(int, input().split()))

for t_R in queries:
    left = 0
    right = n - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == t_R: 
            found = True
            break
        elif arr[mid] < t_R:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print("YES")
    else:
        print("NO")
