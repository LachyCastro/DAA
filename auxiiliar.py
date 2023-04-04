
def is_subs(str_a, str_b):
    """Return True if str_a is a subsequence of str_b

    Args:
        str_a (_str_): _description_
        str_b (_str_): _description_

    Returns:
        _bool_: _description_
    """
    index = 0
    for x in str_b:
        if str_a[index] == x:
            index += 1
        if index == len(str_a):
            return True
    return index == len(str_a)


def balance_result(string: str):
    balance_factor = 0
    result = ""
    for i, par in enumerate(string):
        if par == '(':
            balance_factor += 1
            result += '('
        if par == ')' and balance_factor == 0:
            result += '()'
            continue
        elif par == ')':
            result += ')'
            balance_factor -= 1

    while balance_factor > 0:
        result += ')'
        balance_factor -= 1
    return result


"""def scs(str1, str2):
    INF = 1000
    dp = [[[INF] * 210 for _ in range(210)] for _ in range(210)]
    prv = [[[None] * 210 for _ in range(210)] for _ in range(210)]
    dp[0][0][0] = 0


    len_str1 = len(str1)
    len_str2 = len(str2)

    str1 += "#"
    str2 += "#"
    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            for k in range(201):
                # add "("
                k2 = k + 1
                i2 = i + (str1[i] == "(")
                j2 = j + (str2[j] == "(")
                if dp[i2][j2][k2] > dp[i][j][k] + 1:
                    dp[i2][j2][k2] = dp[i][j][k] + 1
                    prv[i2][j2][k2] = (i, j, k)
            for k in range(1, 201):
                # add ")"
                k2 = k - 1
                i2 = i + (str1[i] == ")")
                j2 = j + (str2[j] == ")")
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

    return "(" * (ans - len(res) - cnt) + "".join(res[::-1]) + ")" * cnt"""

