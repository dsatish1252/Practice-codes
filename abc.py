a = input()
star = 0
has = 0
for i in a:
    if i == '*':
        star += 1
    elif i == '#':
        has += 1
if star > has:
    print(1)
elif star < has:
    print(-1)
else:
    print(0)