x = input()

result = ""

for i in range(len(x)):
    d = int(x[i])
    inv = 9 - d

    # first digit cannot become 0
    if i == 0 and inv == 0:
        result += x[i]
    else:
        result += str(min(d, inv))

print(result)