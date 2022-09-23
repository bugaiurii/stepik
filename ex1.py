i = 1
x = 1

while x != 0:
    x = int(input())
    if x > 0:
        i = i * x
    elif x < 0:
        continue
print(i)
