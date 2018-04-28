def calc_lengths(x, y):
    len_x = len(x)
    len_y = len(y)
    d = [[0] * len_y for _ in range(len_x)]
    
    for i in range(1, len_x):
        for j in range(1, len_y):
            if x[i] == y[j]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(
                        d[i-1][j],
                        d[i][j-1]
                        )

    return d


d = calc_lengths("delete", "leet")
for row in d:
    print(row)
