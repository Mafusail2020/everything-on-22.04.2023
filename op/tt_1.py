n = int(input())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

matrix = [[0 for _ in range(n)] for row in range(n)]

for i in range(len(matrix)):
    matrix[i][i] = list(reversed(s))[i]

for i in range(1, len(matrix)):

    matrix[i][i-1] = list(reversed(d))[i-1]

for row in matrix:
    print(row)
