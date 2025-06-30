x = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")


for i in notes:

    q = int(x // i)
    r = round(x % i, 2)
    #print(f"q = {q}, r = {r}, i = {i}")
    print(f"{q} nota(s) de R$ {i}.00")
    x = r

print("MOEDAS:")
for i in coins:

    q = int(x / i)
    r = round(x % i, 2)
    #print(f"q = {q}, r = {r}, i = {i}")
    print(f"{q} moeda(s) de R$ {i:.2f}")
    x = r