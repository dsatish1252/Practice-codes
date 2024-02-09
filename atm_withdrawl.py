x = int(input())
y = int(input())
if 0 <= x <= 2000 and 0 <= y <= 2000:
        if x % 5 == 0 and 0.5 + x <= y:
                print(float(x) + 0.5)
                print((y-float(x)-0.5))
        else :
            print(y)