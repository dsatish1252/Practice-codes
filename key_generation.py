n1, n2, n3 = map(int, input().split())
flag = True
if 1000 <= n1 <= 9999:
    if 1000 <= n2 <= 9999:
        if 1000 <= n3 <= 9999:
            x = []
            y = []
            def digi(n):
                sml = []
                while n != 0:
                    r = n % 10
                    sml.append(r)
                    n = n // 10
                sml.sort()
                x.append(sml[-1])
                y.append(sml[-2])
            digi(n1)
            digi(n2)
            digi(n3)
            print(f"{sum(x)-sum(y)}")
            flag = False
if flag:
    print(-1)
