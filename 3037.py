N = int(input())

for i in range(N):
    JOAO = 0
    MARIA = 0
    #JOAO
    for i in range(3):
        a,b = map(int, input().split())
        JOAO += a*b
    #MARIA
    for i in range(3):
        a,b = map(int, input().split())
        MARIA += a*b

    #print(JOAO)
    #print(MARIA)
    
    if JOAO > MARIA:
        print("JOAO")
    if MARIA > JOAO:
        print("MARIA")