"""
Result of filled Matrix 7x7:

1  2  3  4  5  6  7
24 25 26 27 28 29 8
23 40 41 42 43 30 9
22 39 48 49 44 31 10
21 38 47 46 45 32 11
20 37 36 35 34 33 12
19 18 17 16 15 14 13
"""
cnt = 1
n = 7

# Init empty matrix
val = [0] * n
for i in range(n):
    val[i] = [0] * n

# Actual logic
for x in range(n // 2):
    # Top line
    for i in range(x, n - 1 - x):
        val[x][i] = cnt
        cnt = cnt + 1

    # Right Line
    for i in range(x, n - 1 - x):
        val[i][n - 1 - x] = cnt
        cnt = cnt + 1

    # Bottom Line
    for i in range(x, n - 1 - x):
        val[n - 1 - x][n - 1 - i] = cnt
        cnt = cnt + 1

    # Left Line
    for i in range(x, n - 1 - x):
        val[n - 1 - i][x] = cnt
        cnt = cnt + 1

# The most center element if it's odd number of N
if n % 2 == 1:
    val[n//2][n//2] = cnt

# Printing results
print(f"\nResult Matrix {n}x{n}:\n")
for i in range(n):
    print(*val[i])