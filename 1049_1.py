word1 = input()
word2 = input()
word3 = input()

if word1 == 'vertebrado':
    if word2 == 'ave':
        if word3 == 'carnivoro':
            print('aguia')

        elif word3 == 'onivoro':
            print('pomba')

    elif word2 == 'mamifero':
        if word3 == 'onivoro':
            print('homem')

        elif word3 == 'herbivoro':
            print('vaca')


elif word1 == 'invertebrado':
    if word2 == 'inseto':
        if word3 == 'hematofago':
            print('pulga')

        elif word3 == 'herbivoro':
            print('lagarta')

    elif word2 == 'anelideo':
        if word3 == 'hematofago':
            print('sanguessuga')

        elif word3 == 'onivoro':
            print('minhoca')
