def best_align(s1, s2, match, mismatch, gap_open, gap_extend):

    m, n = len(s1), len(s2)
    neg = float('-inf')

    M, X, Y = 0, 1, 2

    dpM = [[neg]*(n+1) for _ in range(m+1)]
    dpX = [[neg]*(n+1) for _ in range(m+1)]
    dpY = [[neg]*(n+1) for _ in range(m+1)]

    trM = [[None]*(n+1) for _ in range(m+1)]
    trX = [[None]*(n+1) for _ in range(m+1)]
    trY = [[None]*(n+1) for _ in range(m+1)]

    dpM[0][0] = 0

    for i in range(1, m+1):
        dpX[i][0] = gap_open + (i-1)*gap_extend
        trX[i][0] = M if i == 1 else X

    for j in range(1, n+1):
        dpY[0][j] = gap_open + (j-1)*gap_extend
        trY[0][j] = M if j == 1 else Y

    for i in range(1, m+1):
        for j in range(1, n+1):

            sc = match if s1[i-1] == s2[j-1] else mismatch

            a = dpM[i-1][j-1]
            b = dpX[i-1][j-1]
            c = dpY[i-1][j-1]

            if a >= b and a >= c:
                dpM[i][j] = a + sc
                trM[i][j] = M
            elif b >= c:
                dpM[i][j] = b + sc
                trM[i][j] = X
            else:
                dpM[i][j] = c + sc
                trM[i][j] = Y

            open1 = dpM[i-1][j] + gap_open
            ext1 = dpX[i-1][j] + gap_extend

            if open1 > ext1:
                dpX[i][j] = open1
                trX[i][j] = M
            else:
                dpX[i][j] = ext1
                trX[i][j] = X

            open2 = dpM[i][j-1] + gap_open
            ext2 = dpY[i][j-1] + gap_extend

            if open2 > ext2:
                dpY[i][j] = open2
                trY[i][j] = M
            else:
                dpY[i][j] = ext2
                trY[i][j] = Y

    endM = dpM[m][n]
    endX = dpX[m][n]
    endY = dpY[m][n]

    if endM >= endX and endM >= endY:
        state = M
        score = endM
    elif endX >= endY:
        state = X
        score = endX
    else:
        state = Y
        score = endY

    i, j = m, n
    a1, a2 = [], []

    while i > 0 or j > 0:

        if state == M:
            prev = trM[i][j]
            a1.append(s1[i-1])
            a2.append(s2[j-1])
            i -= 1
            j -= 1

        elif state == X:
            prev = trX[i][j]
            a1.append(s1[i-1])
            a2.append('-')
            i -= 1

        else:
            prev = trY[i][j]
            a1.append('-')
            a2.append(s2[j-1])
            j -= 1

        state = prev

    return score, ''.join(reversed(a1)), ''.join(reversed(a2))
