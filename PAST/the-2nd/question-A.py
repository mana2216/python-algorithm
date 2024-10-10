S, T = input().split()
ans = 0

if "B" in S:
    if "B" in T:
        ans = int(T[1]) - int(S[1]) if int(S[1]) < int(T[1]) else int(S[1]) - int(T[1])
    else:
        ans = int(S[1]) + int(T[0]) - 1
else:
    if "B" in T:
        ans = int(T[1]) + int(S[0]) - 1
    else:
        ans = int(T[0]) - int(S[0]) if int(S[0]) < int(T[0]) else int(S[0]) - int(T[0])

print(ans)