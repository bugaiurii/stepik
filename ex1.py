n = int(input())
i = 1
sum = 0
while i <= n:
    sum = sum + (1/i)
    i += 1
print(round(sum, 3))