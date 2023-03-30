num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
def mutiplo (num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
print(mutiplo(num1, num2))