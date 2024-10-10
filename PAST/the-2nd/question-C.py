N = int(input())
grid = []
for i in range(N):
    grid.append(list(input()))

for i in range(N-2, -1, -1):
    for j in range(0, N*2-1):
        if grid[i][j] == "X":
            continue

        if grid[i][j] == "#" and 0 <= (j - 1) and grid[i+1][j-1] == "X":
            grid[i][j] = "X"
            continue

        if grid[i][j] == "#" and grid[i+1][j] == "X":
            grid[i][j] = "X"
            continue

        if grid[i][j] == "#" and (j + 1) < (N * 2 - 1) and grid[i+1][j+1] == "X":
            grid[i][j] = "X"
            continue

for i in range(N):
    for j in range(N * 2 - 1):
        print(grid[i][j], end="")
    print()