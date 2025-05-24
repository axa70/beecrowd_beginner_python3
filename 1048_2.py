N = float(input())

salarpercent_adjust = [0,400, 800, 1200, 2000]
percentage = [15,12,10,7,4]

adjusted_val = 0
for i in range(4):

    if N>2000:
        adjusted_val = N*percentage[-1]/100
        break

    elif (N>salarpercent_adjust[i] and N<=salarpercent_adjust[i+1]):
        adjusted_val = N*percentage[i]/100
        break

new_sal = adjusted_val + N
percent_adjust = percentage[i]

print(f"New sal = {new_sal}")
print(f"adjust = {adjusted_val}")
print(f"percentage = {percent_adjust}")
