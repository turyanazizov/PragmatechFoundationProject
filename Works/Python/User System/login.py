from data import users

def userLogin(count):
    tapildi=False
    username=input('Username daxil edin :')
    password=input('Sifrenizi daxil edin :')

    for index in range(len(users)):

        if users[index].username==username and users[index].password==password:
            print('Sisteme daxil oldunuz, melumatlariniz : ')
            print('||', users[index].ad, ' || ' , users[index].soyad, ' || ' )
            tapildi=True
            change(index)            
        if count==3:
            print('Siz 3 haqqinizdan istifade etdiniz.Sistem Blok edildi!!!')
            break

        if tapildi==False and index==len(users)-1:
            print(f'Yanlis melumat daxil etdiniz!Qalan cehd sayiniz - {3-count}')
            return userLogin(count+1)

def change(index):
    print("""
                1.Istifadeci adinizi deyisin
                2.Sifrenizi deyisin
                3.Esas menyuya qayidin
                """)
    emr=input('Emeliyyat kodunu yazin : ')
    if emr=='1':
        newUsername=input('Yeni istifadeci adinizi daxil edin : ')
        users[index].username=newUsername
        print('Istifadeci adiniz deyisdirildi!!!')
    elif emr=='2':
        newPass=input('Yeni sifrenizi daxil edin : ')
        users[index].password=newPass
        print('Sifreniz deyisdirildi!!!')
    else:
        return