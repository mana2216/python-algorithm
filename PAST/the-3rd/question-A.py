s = input()
t = input()
flag = True
for i in range(len(s)):
    if s[i] != t[i]:
        flag = False
        break

if flag:
    print("same")
    exit()

flag = True

s_upper = s.upper()
t_upper = t.upper()

for i in range(len(s_upper)):
    if s_upper[i] != t_upper[i]:
        flag = False
        break

if flag:
    print("case-insensitive")
    exit()

print("different")