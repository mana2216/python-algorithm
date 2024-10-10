S = input()
num = 0
for ch in S:
    if ord('a') <= ord(ch) <= ord('z'):
        print("error")
        exit()

    num = num * 10 + int(ch)

ans = num * 2

print(ans)