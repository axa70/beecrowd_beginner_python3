Ball_old = int(input())
Branch = int(input())

Ball_req = int(Branch / 2)

Ball_new = Ball_req - Ball_old

if Ball_new > 0:
    print(f"Faltam {Ball_new} bolinha(s)")

else:
    print(f"Amelia tem todas bolinhas!")
