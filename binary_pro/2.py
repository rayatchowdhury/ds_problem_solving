n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    left = 0
    right = n - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= q:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans + 1)