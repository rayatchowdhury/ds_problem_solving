t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')


    ans = min(n - r, n - g, n - b)
    print(ans)