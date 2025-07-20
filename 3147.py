H, E, A, O, W, X = map(int, input().split())

g = H+E+A+X
e = O+W

if g>e:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")