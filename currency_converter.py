inr = int(input())
curr = input()
dict = {"euro":0.01417,"british pound":0.0100,"australian dollar":0.02140,"canadian dollar":0.02027}
if curr in dict:
    print(inr*dict[curr])
else :
    print(-1)