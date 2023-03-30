num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def maximo(num1, num2):
    if num1 > num2:
        print(f'O {num1} é maior que o {num2}')
    elif num1 < num2:
        print(f'O {num1} é menor que {num2}')
maximo(num1,num2)