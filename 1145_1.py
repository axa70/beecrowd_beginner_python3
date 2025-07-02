#solved by chatgpt
col, num = map(int, input().split())

for i in range(1, num+1):
    print(f"{i}", end="")

    if i%col==0:
        print()
    else:
        print(" ", end="")