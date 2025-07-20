try:
    M = int(input())
    values=[]
    for i in range(M):
        v = int(input())
        values.append(v)

    step = int(input())

    sum_l= values[::-step]
    result=sum(sum_l)

    #print(sum_l)
    #print(result)

    prime = True

    if result<2 or result==2 or result%2==0:
        prime = False
    else:
        for i in range(3,int(result ** 0.5) + 1,2):
            if result%i==0:
                prime = False
                break
    '''
    if prime == True: print("prime")
    else: print("not prime")
    '''

    if prime == True: 
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else: print("Bad boy! I’ll hit you.")

except EOFError:
    exit()
