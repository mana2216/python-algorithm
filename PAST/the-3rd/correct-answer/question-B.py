from collections import defaultdict

def print_score(scores, solved, n):
    result = 0
    for item in solved[n]:
        result += scores[item]
    print(result)

def solved_problem(scores, solved, n, m):
    solved[n].append(m)
    scores[m] = scores[m] - 1 if scores[m] > 0 else 0

def main():
    N,M,Q = map(int, input().split())
    scores = [N] * M
    solved = defaultdict(list)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            n = query[1] - 1
            print_score(scores, solved, n)
        elif query[0] == 2:
            n = query[1] - 1
            m = query[2] - 1
            solved_problem(scores, solved, n, m)

main()