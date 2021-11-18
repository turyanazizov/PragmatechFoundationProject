users=[]
def addUser():
    _ad=input('Istifadəçi adı:')
    _soyad=input('Istifadəçi soyadı:')
    user={
        'ad':_ad,
        'soyad':_soyad
    }
    users.append(user)

def showUsers():
    for index in range(len(users)):
        print('Istifadəçi No: ',index)
        print('Istifadəçi adi: ',users[index]['ad'])
        print('Istifadəçi adi: ',users[index]['soyad'])
        print('-------------------------------')

def deleteUser():
    nomre=input('Silmek istediyiniz istifadecinin nomresini yazin: ')
    users.pop(int(nomre))
    print('Istifadəçi silindi')
    print('-------------------------------')

def editUser():
    nomre=input('Deyismek istediyiniz istifadecinin nomresini yazin: ')
    yeniAd=input('Yeni adi daxil edin: ')
    yeniSoyad=input('Yeni soyadi daxil edin: ')
    users[int(nomre)]['ad']=yeniAd
    users[int(nomre)]['soyad']=yeniSoyad
    print('Istifadəçi məlumatları dəyişdirildi')
    print('-------------------------------')

menyu="""
--------------------------------------------------------
                    Proqram Ana Sehifə
- Yeni istifadəçi əlavə etmək üçün --1-- yazin
- Var olan istifadəçiləri görmək üçün --2-- yazin
- İstifadəçi silmək üçün --3-- yazin
- İstifadəçi məlumatlarini deyismek ucun --4-- yazin
- Proqramı dayandırmaq üçün --5-- yazın
--------------------------------------------------------
"""

while True:
    print(menyu)
    emeliyat=input("Istediyiniz emeliyat kodunu yazin :")
    if emeliyat=='1':
        addUser()
    elif emeliyat=='2':
        showUsers()
    elif emeliyat=='3':
        deleteUser()
    elif emeliyat=='4':
        editUser()
    elif emeliyat=='5':
        break
    else:
        pass