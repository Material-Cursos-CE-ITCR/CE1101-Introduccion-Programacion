import sys

num =121182393281121
strNum ="121182393281121"
listNum =[1,2,1,1,8,2,3,9,3,2,8,1,1,2,1]

print(num, sys.getsizeof(num))
print(strNum, sys.getsizeof(strNum))
print(listNum, sys.getsizeof(listNum))

#########################################################
# Version 2. Usando listas y subindices                 #
#########################################################

def checkPalindromo_aux(listNum):
    print("Num: ",listNum)
    print("Len: ",len(listNum))

    print("i: ",listNum[0])
    print("j: ",listNum[-1])
    if(listNum == [] or len(listNum) <= 1):
        return True
    elif(listNum[0] == listNum[-1]):
        listNum = listNum[1:-1]
        return True and checkPalindromo_aux(listNum)
    else:
        return False
    
def checkPalindromo(num):
    if(isinstance(num, int) and (num > 10 or num < -10)):
        listNum = list(str(abs(num)))
        return checkPalindromo_aux(listNum)
    else:
        return False
    
print(123454321, checkPalindromo(123454321))
print(121, checkPalindromo(121))
print(12345678, checkPalindromo(12345678))
print('123321', checkPalindromo('123321'))