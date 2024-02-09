fdcost = 0
cost = 0
decide = input().upper()
qty = int(input())
km = int(input())
if decide == "V" or decide == "N":
    if km >0 and qty > 0:
        if decide  == "V":
            cost = 120 * qty
        else :
            cost = 150 * qty
        if km <= 3:
            fdcost = fdcost
        elif (km > 3 and km <= 6) :
            fdcost = (km - 3) * 3
        elif km > 6:
            fdcost = 0 +  3 * 3 + (km - 6) * 6
        print(fdcost+cost)
    else :
        print(-1)
else:
    print(-1)