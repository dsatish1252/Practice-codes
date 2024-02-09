x = int (input())
y = int (input())
z = int (input())
a = x * 5 + y * 1
b = z % 5
if a < z or b > y:
    print(-1)
else:
    print(z % 5)
    print(z // 5)