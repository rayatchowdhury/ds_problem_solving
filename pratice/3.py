t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    t_str = input()

    diff = 0
    for i in range(n):
        if s[i] != t_str[i]:
            diff += 1

    if diff >= 2 and t_str.count('o') > 0:
        print("YES")
    else:
        print("NO")