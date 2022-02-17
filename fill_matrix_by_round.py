#
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

if n % 2 == 1:
    val[n//2][n//2] = cnt

# Printing results
print(f"\nResult Matrix {n}x{n}:\n")
for i in range(n):
    print(*val[i])