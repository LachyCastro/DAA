import utils



LENGTH = 0
SOLUTION = ''

def generate(left, right, n, s, A, B): #Bactraking
    global LENGTH
    global SOLUTION
    if left == n and right == n:
        if utils.verify_solution(s, A) and utils.verify_solution(s, B):
            LENGTH = len(s) 
            SOLUTION = s
            raise utils.Done 
        return

    if left < n:
       generate(left + 1, right, n, s + '(', A, B)
    if right < left:
        generate(left, right + 1, n, s + ')', A, B)
        

def basic_solution(left, right, n, s, A, B): #Este metodo es usado para capturar la primera sol y parar ya q solo importa el len
    try: 
        generate(left, right, n, s, A, B)
    except utils.Done:
        pass
    


