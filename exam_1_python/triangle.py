def triangle(n):
    row = []
    rows = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
        rows.append(row)
    return rows[n - 1]