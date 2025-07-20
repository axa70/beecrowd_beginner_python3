N = int(input())

numbers = [1]

for i in range(N-1):
    if i == 0:
        result = 1
    
    if i > 0:
        result = numbers[i-1] + numbers[i]
    
    #print(result)
    numbers.append(result)
    

numbers.sort(reverse = True)   
result_str = ' '.join(map(str, numbers)) 
print(result_str)

    