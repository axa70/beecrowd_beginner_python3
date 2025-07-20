t_c = int(input())

for i in range(t_c):
    input_list = list(map(int, input().split()))

    n = input_list[0]
    total = 0
    for i in range(1,n):
        total += input_list[i] - 1

    result = total + input_list[-1]
    print(result)