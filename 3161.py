#01 Very clever program
#https://github.com/gabzintav/beecrowd/blob/main/3161.py

#02 Easy to understand program
#https://github.com/Boombarm/onlinejudge/blob/master/Python/src/uri_beecrowd/BEGINNER/P3161_The_Forgotten_Fruits.py

#03 Program solved using sets
#https://github.com/gustavonikov/URI_problems/blob/main/URI%203161%20-%20The%20Forgotten%20Fruits.py

#I like 02

def reverse(s: str):
    return s[::-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    fruitList = []
    db = []
    for i in range(n):
        c = input().lower()
        fruitList.append(c)

    for i in range(m):
        c = input().lower()
        db.append(c)

    for fruit in fruitList:
        chk = 0
        for data in db:
            if fruit in data:
                chk = 1
                break
            if fruit in reverse(data):
                chk = 1
                break
            if reverse(fruit) in data:
                chk = 1
                break
            if reverse(fruit) in reverse(data):
                chk = 1
                break
        if chk == 1:
            print('Sheldon come a fruta %s' % fruit)
        else:
            print('Sheldon detesta a fruta %s' % fruit)