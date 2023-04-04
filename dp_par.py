STRING_A = ")(())"
STRING_B = "())))"


def solve(str1, str2):
    INF = 1000
    dp = [[[INF] * 310 for _ in range(310)] for _ in range(310)]
    prv = [[[None] * 310 for _ in range(310)] for _ in range(310)]
    dp[0][0][0] = 0

    len_str1 = len(str1)
    len_str2 = len(str2)

    str1 += "#"
    str2 += "#"
    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            for k in range(301):
                # add "("
                k2 = k + 1
                i2 = i
                j2 = j
                if str1[i] == "(":
                    i2 = i + 1
                if str2[j] == "(":
                    j2 = j + 1
                if dp[i2][j2][k2] > dp[i][j][k] + 1:
                    dp[i2][j2][k2] = dp[i][j][k] + 1
                    prv[i2][j2][k2] = (i, j, k)
            for k in range(1, 301):
                # add ")"
                k2 = k - 1
                i2 = i
                j2 = j
                if str1[i] == ")":
                    i2 = i + 1
                if str2[j] == ")":
                    j2 = j + 1
                if dp[i2][j2][k2] > dp[i][j][k] + 1:
                    dp[i2][j2][k2] = dp[i][j][k] + 1
                    prv[i2][j2][k2] = (i, j, k)

    ans = INF
    cnt = 0
    for c, val in enumerate(dp[len_str1][len_str2]):
        if c + val < ans + cnt:
            ans = val
            cnt = c

    res = []
    i, j, k = len_str1, len_str2, cnt

    while i > 0 or j > 0 or k > 0:
        prv_i, prv_j, prv_k = prv[i][j][k]
        if prv_k < k:
            res.append("(")
        else:
            res.append(")")
        i, j, k = prv_i, prv_j, prv_k

    return "(" * (ans - len(res) - cnt) + "".join(res[::-1]) + ")" * cnt


#print(solve(STRING_A, STRING_B))

