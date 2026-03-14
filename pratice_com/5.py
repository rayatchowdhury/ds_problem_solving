l = int(input())

for _ in range(l): 
    num = int(input())
    good = True
    for num2 in range(2, num):
        if num < 2:
            good = False
        if num % num2 != 0:
            good = False
        else:
            good = True

    if good:
        print("yes")
    else: 
        print("NO")