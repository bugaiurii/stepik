n = int(input())
i = 1
mylist = []

if n >= 100:
    print(f'слишком большое значение n')
else:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            mylist.append(i)
        i += 1
    else:
        print(*mylist)






