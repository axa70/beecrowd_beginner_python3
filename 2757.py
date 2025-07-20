A = int(input())
B = int(input())
C = int(input())
print(f"A = {A}, B = {B}, C = {C}")

print(f"A = {A:>10}, B = {B:>10}, C = {C:>10}")
print(f"A = {str(A).zfill(10)}, B = {str(B).zfill(10)}, C = {str(C).zfill(10)}")
print(f"A = {A:<10}, B = {B:<10}, C = {C:<10}")
