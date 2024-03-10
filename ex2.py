def check_fibo(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False
    
def produce_result(n):
    if check_fibo(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

produce_result(int(input("Informe o número que deseja verificar se está presente na sequência de Fibonacci: ")))
