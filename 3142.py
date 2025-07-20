#https://github.com/gustavonikov/URI_problems/blob/main/URI%203142%20-%20Excel%20Bug.py

while True:
    try:
        S = input()

        if len(S) == 1:
            result = ord(S) - 64
            print(result)
            
        elif len(S) == 2:
            n = (ord(S[0]) - 64) * 26

            result = n + (ord(S[1]) - 64)
            print(result)

        elif len(S) == 3:
            n1 = ord(S[0]) - 64
            n2 = ord(S[1]) - 64
            n3 = ord(S[2]) - 64

            result = n1 * 26**2 + n2 * 26 + n3

            if result <= 16384:
                print(result)
            else:
                print('Essa coluna nao existe Tobias!')
                
        elif len(S) > 3:
            print('Essa coluna nao existe Tobias!')

    except EOFError:
        break