s = input().upper()
s += " "
i = 0
count = 1
n = ''
while i < len(s) - 1:
    if s[i] == s[i+1]:
        count += 1
    else:
        n += f"{count}{s[i]}"
        count = 1
    i += 1
print(n)
