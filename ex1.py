city = input().split()
i = 0
while i < len(city):
    if len(city[i]) < 6:
        print('НЕТ')
        break
    i += 1
else:
    print('ДА')
