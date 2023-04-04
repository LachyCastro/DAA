import json
from colorama import Fore
from dp_par import solve 
import recursive_par
import utils
def test_dp(name):
    f = open(name+'.json')
    data = json.load(f)
    print('Probandp casos desde', name+'.json')
    for ind, case  in enumerate(data['cases']):
        if case['Sol'] != '':
            dp_sol = solve(case['A'],case['B'])
            if len(dp_sol) == len(case['Sol']):
                print(ind ,"\033[92m {}\033[00m" .format("Bien"))
            else:
                print(ind, "\033[91m {}\033[00m" .format("Mal"))

def test_recursive(name):
    f = open(name+'.json')
    data = json.load(f)
    print('Probandp casos desde', name+'.json')
    for ind, case  in enumerate(data['cases']):
        if case['Sol'] != '':
            A = case['A']
            B = case['B']
            recursive_par.BEST_RESULT = recursive_par.balance_result(A + B)
            recursive_par.recursive_solution(A, B, 0, 0, "")
            res = recursive_par.balance_result(recursive_par.BEST_RESULT)
            if utils.verify_solution(res, A) and utils.verify_solution(res, B):
                if len(res) == len(case['Sol']):
                    print(ind ,"\033[92m {}\033[00m" .format("Bien"))
                else:
                    print(ind, "\033[91m {}\033[00m" .format("Mal"))
            else:
                print(ind, "\033[91m {}\033[00m" .format("Mal"))

test_dp('cases')
test_dp('recursive_cases')
test_recursive('cases')
