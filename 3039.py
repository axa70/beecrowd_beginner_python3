N = int(input())
car = 0
doll = 0
for i in range(N):

    name, gender = input().split()

    if gender == "M":
        car += 1
    if gender == "F":
        doll += 1

print(f"{car} carrinhos")
print(f"{doll} bonecas")