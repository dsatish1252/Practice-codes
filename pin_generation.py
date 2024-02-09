alpha = int(input("alpha="))
beta = int(input("beta="))
gamma = int(input("gamma="))

l = []
s = ''
for i in range(len(str(alpha))):
    s += min(str(alpha)[i], str(beta)[i], str(gamma)[i])
    l.append(str(alpha)[i])
    l.append(str(beta)[i])
    l.append(str(gamma)[i])

x = max(l)
s = x + s
print(f"PIN={s}")
