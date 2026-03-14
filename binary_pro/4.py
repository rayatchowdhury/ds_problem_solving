n = int(input())
arr = list(map(int, input().split()))

arr.sort()

k = int(input())

for _ in range(k):
    l, r = map(int, input().split())

    left = 0
    right = n - 1
    left_pos = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= l:
            left_pos = mid
            right = mid - 1
        else:
            left = mid + 1

    left = 0
    right = n - 1
    right_pos = n

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > r:
            right_pos = mid
            right = mid - 1
        else:
            left = mid + 1

    print(right_pos - left_pos, end=" ")