emr=input('Emri daxil edin: ')

def hesabla(a,b):
    if emr=='+':
       return cem(a,b)
    elif emr=='-':
        return ferq(a,b)
    elif emr=='*':
        return vur(a,b)
    elif emr=='/':
        return bol(a,b)
    else:
        return 'Sehv emelyat'

def cem(a,b):
    return a+b
def ferq(a,b):
    return a-b
def vur(a,b):
    return a*b
def bol(a,b):
    return a/b

print(hesabla(10,5))
print(cem(100,40)+ferq(100,40))