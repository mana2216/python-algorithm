N = int(input())
sales = []
for i in range(N):
    sales.append(int(input()))

for i in range(N-1):
    if sales[i] < sales[i+1]:
        print("up", sales[i+1] - sales[i])
    elif sales[i] > sales[i+1]:
        print("down", sales[i] - sales[i+1])
    else:
        print("stay")