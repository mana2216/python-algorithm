S = input()
for ch in S:
    if ord('a') <= ord(ch) <= ord('z'):
        print("error")
        exit()

ans = int(S) * 2

print(ans)