n=int(input())
arr=[]

for i in range(n):
        arr.append(input())

def checkFirstDigit(element):
    if element[0]=='7' or element[0]=='8' or element[0]=='9':
        return True
    else:
        return False

def checkLen(element):   
    if len(element)==10:
        return True
    else:
        return False

def checkIsDigit(element):
    if element.isdigit():
        return True
    else:
        return False

for elem in arr:
    if(checkFirstDigit(elem) and checkLen(elem) and checkIsDigit(elem)):
        print('YES')
    else:
        print('NO')
