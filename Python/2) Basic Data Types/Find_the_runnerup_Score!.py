n = int(input())
if 2 <= n <= 10:
    pass
l = list(map(int, input().split()))
for i in l:
    if -100 <= i <= 100:
        pass
l.sort()
l_s = set(l)
l1 = list(l_s)
updated_list = sorted(l1)
print(updated_list[-2], end="")
