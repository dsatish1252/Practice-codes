a,b = input().split()
a = int(a)
b = int(b)
def prime_check(num):
  for i in range(2,num):
      if num % i == 0:
          return False
  return True
for i in range(a,b):
    if prime_check(i):
        x, s, r = i, 0, 0
        while x > 0:
            r = x % 10
            s = s + r
            x = x // 10
        if prime_check(s):
            print(f"{i}", end=" ")