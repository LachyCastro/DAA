import random
import recursive_par
import utils
import auxiiliar
import basic_sol 

def test(number_of_cases):# Recibe el numero de casos a guardar en el json. Usa la solucion Fuerza Bruta
    data = {
        'cases' : []
    }
    while(number_of_cases > 0 ):
        basic_sol.SOLUTION = ''
        ######################## Recursive Result ######################################
        A_seq = ['(',')'] * random.randrange(1,10)
        B_seq = ['(',')'] * random.randrange(1,10)
        random.shuffle(A_seq)
        random.shuffle(B_seq)
        A_seq = utils.array_str(A_seq)
        B_seq = utils.array_str(B_seq)
        x = max(len(auxiiliar.balance_result(A_seq)), len(auxiiliar.balance_result(B_seq)))
        while basic_sol.SOLUTION == '':
            basic_sol.basic_solution(0, 0, x/2, '', A_seq, B_seq)
            x += 2 
        case = {
            'A' : A_seq,
            'B' : B_seq,
            'Sol' : basic_sol.SOLUTION
        }
        print(number_of_cases)#pa saber por donde va 
        data['cases'].append(case)
        number_of_cases = number_of_cases - 1 
    utils.to_json('cases',data)

def test_recursive(number_of_cases):# Recibe el numero de casos a guardar en el json. Usa la segunda solucion
    data = {
        'cases' : []
    }
    while(number_of_cases > 0 ):
        ######################## Recursive Result ######################################
        A_seq = ['(',')'] * random.randrange(1,20)
        B_seq = ['(',')'] * random.randrange(1,20)
        random.shuffle(A_seq)
        random.shuffle(B_seq)
        A_seq = utils.array_str(A_seq)
        B_seq = utils.array_str(B_seq)
        recursive_par.BEST_RESULT = recursive_par.balance_result(A_seq + B_seq)
        recursive_par.recursive_solution(A_seq, B_seq, 0, 0, 0, "")
        case = {
            'A' : A_seq,
            'B' : B_seq,
            'Sol' : recursive_par.BEST_RESULT
        }
        print(number_of_cases)#pa saber por donde va 
        data['cases'].append(case)
        number_of_cases = number_of_cases - 1 
    utils.to_json('recursive_cases',data)


# test_recursive() #Pasar en ambos el numero de casos de prueba a guardar 
# test()