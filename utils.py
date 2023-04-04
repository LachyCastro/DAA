import json

class Done(Exception):# Manegar cuando parar en la solucion Backtraking
    """Ya encontre la primera solucion"""

def to_json(name,json_string):
    with open(name+'.json', 'w') as outfile:
        json.dump(json_string,outfile)

def verify_solution(solution, A): #Verificar si aparecen las subcadenas
    for  x in solution:
        if len(A) == 0:
            return True
        if x == A[0]:
           A = A[1:]
    if A == '':
        return True
    return False

def array_str(seq_in_array):
    seq_in_str = ''
    for char in seq_in_array:
        seq_in_str += char
    return seq_in_str