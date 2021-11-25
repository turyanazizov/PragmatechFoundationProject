# istifadecinin qeydiyyatdan kecmesi ucun lazim olan kodlar da burda olacaq
from data import User,users

def registerUser():
    ad=input('Adiniz :')
    if checkData(ad)==False:
        print('Sizin qeydiyyatiniz tamamlanmadi.Zehmet olmasa melumatlari duzgun daxil edin')
        ad=input('Adiniz :')
    soyad=input('Soyadiniz :')
    if checkData(soyad)==False:
        print('Sizin qeydiyyatiniz tamamlanmadi.Zehmet olmasa melumatlari duzgun daxil edin')
        soyad=input('Soyadiniz :')
    username=input('Istifadeci adiniz :')
    if checkData(username)==False:
        print('Sizin qeydiyyatiniz tamamlanmadi.Zehmet olmasa melumatlari duzgun daxil edin')
        username=input('Istifadeci adiniz :')
    password=input('Sifreniz :')
    if checkPass(password)==False:
        print('Sizin qeydiyyatiniz tamamlanmadi.Sifrenin uzunlugu 8-den boyuk, terkibinde en az 1 reqem ,1 boyuk herf olmalidir.')
        password=input('Sifreniz :')
    # terminaldan daxil edilen melumatlar esasinda yeni user obyekti yarat
    print('Sizin qeydiyatiniz ugurla basa catdi!!!')
    user=User(ad,soyad,username,password)
    # yaradilan yeni useri users listine elave et
    users.append(user)

def checkData(data):
    if len(data)==0:
        return False
    else:
        return True

def checkPass(data):
    if checkPassLen(data)==True and checkPassDigit(data)==True and checkPassUpper(data)==True:
        return True
    else:
        return False

def checkPassLen(data):
    if len(data)>8:
        return True

def checkPassDigit(data):
    for string in data:
        if string.isnumeric():
            return True

def checkPassUpper(data):
    for string in data:
        if string.isupper():
            return True
    