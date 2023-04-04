from auxiiliar import is_subs, balance_result


def recursive_solution(string_A, string_B, fst_ind, scnd_ind, result):
    global BEST_RESULT
    if fst_ind == len(string_A):
        result = result + string_B[scnd_ind:]
        str_bal = balance_result(result)
        if len(str_bal) <= len(BEST_RESULT):
            BEST_RESULT = str_bal
        return
    if scnd_ind == len(string_B):
        result = result + string_A[fst_ind:]
        str_bal = balance_result(result)
        if len(str_bal) <= len(BEST_RESULT):
            BEST_RESULT = str_bal
        return
    
    # CASO:1 => abierto-abierto, en la solucion va un abierto, +1 factor de balance
    if string_A[fst_ind] == string_B[scnd_ind] and string_A[fst_ind] == "(":
        result = result + "("
        
        recursive_solution(string_A, string_B, fst_ind + 1,
                           scnd_ind + 1, result)
    # CASO:2 => cerrado-cerrado, en la solucion va un cerrado, -1 factor de balance
    if string_A[fst_ind] == string_B[scnd_ind] and string_A[fst_ind] == ")":  # factor de balance > 0?
        result = result + ")"
        recursive_solution(string_A, string_B, fst_ind + 1,
                           scnd_ind + 1, result)
    elif string_A[fst_ind] != string_B[scnd_ind]:
        if string_A[fst_ind] == ')':  # fact_balance > 0?
            result = result + ')'
            
            recursive_solution(string_A, string_B, fst_ind +
                               1, scnd_ind, result)
            
            result = result[:len(result) - 1]
            result += '('
            recursive_solution(string_A, string_B, fst_ind,
                               scnd_ind + 1, result)
        else:
            result = result + '('
            
            recursive_solution(string_A, string_B, fst_ind +
                               1, scnd_ind, result)
            
            result = result[:len(result) - 1]
            result = result + ')'
            recursive_solution(string_A, string_B, fst_ind,
                               scnd_ind + 1, result)


# STRING_A = "))))"
# STRING_B = "(((("
# BEST_RESULT = balance_result(STRING_A + STRING_B)

# recursive_solution(STRING_A, STRING_B, 0, 0, "")
# res = balance_result(BEST_RESULT)
# print(res)
# print(len(res))
