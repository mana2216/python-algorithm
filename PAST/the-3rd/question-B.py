N, M, Q = map(int, input().split())

# 問題の解答者を格納
question_dict = {}

# 問題の持つポイントを格納
q_points_dict = {}

for i in range(1, M + 1):
    question_dict[i] = []
    q_points_dict[i] = N

# 各解答者のポイントを格納
answerer_dict = {}

for i in range(1, N + 1):
    answerer_dict[i] = {}
    for j in range(1, M + 1):
        answerer_dict[i][j] = 0

for i in range(Q):
    q_list = list(map(int, input().split()))
    if q_list[0] == 1:
        n = q_list[1]
        ans_point = 0
        for i in range(1, M + 1):
            ans_point += answerer_dict[n][i]
        print(ans_point)
    elif q_list[0] == 2:
        n = q_list[1]
        m = q_list[2]
        question_dict[m].append(n)
        q_points_dict[m] = q_points_dict[m] - 1 if q_points_dict[m] > 0 else 0
        for item in question_dict[m]:
            answerer_dict[item][m] = q_points_dict[m]
