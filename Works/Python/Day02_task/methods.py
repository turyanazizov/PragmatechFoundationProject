adlar=[
    'Ali',#len=3
    'Mehdi',#len=5
    'Senan',#len=5
    'Mirbaba',#len=7
    'Ulvi',#len=4
    'Seyyad',#len=6
    'Turyan'#len=6
]
# Butun adlari ekrana cap eden metod yazin adlariGoster()
print("Butun adlar: ")
def adlariGoster(names):
    for name in names:
        print(name)
adlariGoster(adlar)
# Listin cut yerde duran elementlerini gosteren metod yazin cutYerdekiler()
print("Cut yerdekiler: ")
def cutYerdekiler(names):
    for i in range(1,len(names)):       
        if i%2==0:
            print(names[i])
cutYerdekiler(adlar)
# Listi elifba sirasina gore siralayan metod yazin listiSirala()
print('Elifba sirasina gore ardicilliq: ')
def listiSirala(names):
    names.sort()
    print(names)
listiSirala(adlar)
# Daxilində e herfi olan adları ekrana cap edən metod yazin
print('Daxilinde e herifi olan adlar: ')
def find_e(names):
    for name in names:
        for i in range(len(name)):
            if(name[i]=='e'):
                print(name)
find_e(adlar)
# Son hərfi i olan adlari ekrana cap eden metod yazin
print('Son herfi i olan adlar: ')
def last_i(names):
    for name in names:
        if name[len(name)-1]=='i':
            print(name)
last_i(adlar)
# Hərf sayi eyni olan nece ad oldugunu ekrana cap edin
print('Herf sayi eyni olan nece ad var: ')
def countSameLen(names):
    count=0
    for name in names:
        for ad in names:
            if len(name)==len(ad) and name!=ad:
                count+=1
                print(name,'|',ad)
                break
    print(count)
countSameLen(adlar)
