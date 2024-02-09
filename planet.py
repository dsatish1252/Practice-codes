days = int(input())
radius = []
gms = []
for i in range(0,days):
    a,b = input().split()
    a = int(a)
    b = int(b)
    radius.append(a)
    gms.append(b)
total_mtrs = 0
for i in gms:
    total_mtrs = i * 100
cir_per = 0
for i in radius:
    cir_per += 2 * (22/7) * i
toffes = total_mtrs // cir_per
print(int(toffes))