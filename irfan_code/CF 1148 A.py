a, b, c = map(int, input().split())

ans = 2 * c
ans += 2 * min(a, b)

if a != b:
    ans += 1

print(ans)