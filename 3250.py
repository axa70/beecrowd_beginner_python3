f, s, g, u, d = map(int, input().split())

if u == 0 or d == 0 or (g %2 != 0 and u %2 == 0 and d %2 == 0) or (s %2 != 0 and u %2 == 0 and d %2 == 0):
    print("use the stairs")

else:
    count = 0
    curr_level = s
    while True:
        if g>curr_level:
            curr_level += u
            count += 1
        if g<curr_level:
            curr_level -= d
            count += 1
        #print(curr_level)

        if curr_level == g:
            break

    print(count)
        