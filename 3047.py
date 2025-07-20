m = int(input())
a = int(input())
b = int(input())

c = m - a - b

oldest = [a,b,c]
oldest.sort()
print(oldest[2])