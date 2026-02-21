x = input()

result = ""

for i in range(len(x)):
    d = int(x[i])
    inv = 9 - d

    if i == 0 and inv == 0:
        result += x[i]
    else:
        result += str(min(d, inv))

print(result)