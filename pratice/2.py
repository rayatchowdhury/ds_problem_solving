n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

even_c = 0
odd_c = 0
even_k = 0
odd_k = 0
for x in a:
    if x % 2 == 0:
        even_c += 1
    else:
        odd_c += 1

for x in b:
    if x % 2 == 0:
        even_k += 1
    else:
        odd_k += 1

result = min(even_c, odd_k) + min(odd_c, even_k)

print(result)