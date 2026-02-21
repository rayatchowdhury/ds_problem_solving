n = int(input())
a = list(map(int, input().split()))

mn = min(a)
mx = max(a)

print(mx - mn + 0 - n)