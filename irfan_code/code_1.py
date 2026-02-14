input_0 = int(input())
 
for _ in range(input_0):
    ts_1 = int(input())
 
    if ts_1 % 2 == 1:
        print("7", end="")
        ts_1 -= 3
 
    print("1" * (ts_1 // 2))
