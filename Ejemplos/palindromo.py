#########################################################
# Version 1. Usando función módulo y división entera    #
#########################################################

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

def checkPalindromo_aux(num, lenNum):
    print("Num: ",num)
    print("Len: ",lenNum)

    print("i: ",num%10)
    print("j: ",num//10**(lenNum-1))
    # Casos bases si la cantidad de dígitos es par o impar
    if(lenNum == 0 or lenNum == 1):
        return True
    # Revisar si el ultimo y el primer elemento iguales
    elif(num%10 == num//10**(lenNum-1)):
        num = num%10**(lenNum-1)    # Eliminar el último número
        num = num//10               # Eliminar el primer número
        return True and checkPalindromo_aux(num, lenNum-2) # Quitamos 2 dígitos del número
    else:
        return False
    
def checkPalindromo(num):
    if(isinstance(num, int) and num > 10):
        num = abs(num)
        cantDigitos = count_digits(num)
        return checkPalindromo_aux(num, cantDigitos)
    else:
        return False


print(123454321, checkPalindromo(123454321))
print(121, checkPalindromo(121))
print(12345678, checkPalindromo(12345678))
print('123321', checkPalindromo('123321'))