from collections import defaultdict

S = input()
candidate = defaultdict(int)

for item in S:
    candidate[item] += 1

ans = ""
max_num = -1

for key, value in candidate.items():
    if max_num < value:
        max_num = value
        ans = key

print(ans)