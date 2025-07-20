#https://github.com/mcavalca/uri-python/blob/master/2782.py

N = int(input())
sequence = list(map(int, input().split()))
result = 1
if N == 1 or N == 2:
    print(1)

else:
    for i in range(2,N):
        if sequence[i] - sequence[i-1] != sequence[i-1] - sequence[i-2]:
            result += 1

    print(result)
