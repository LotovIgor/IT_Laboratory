def matrix (M1, M2):
    M = []
    for i in range(d):
        M.append([])
    sum = 0
    for k in range(d):
        for i in range(d):
            for j in range(d):
                sum += M1[k][j] * M2[j][i]
            M[k].append(sum)
            sum = 0
    return M


M1 = [[5, 8, -4],
      [6, 9, -5],
      [4, 7, -3]]
M2 = [[3, 2, 5],
      [4, -1, 3],
      [9, 6, 5]]
d = len(M1)

print(matrix(M1, M2))
