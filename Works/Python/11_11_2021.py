telebeler = [
    {
        'ad': 'Samir',
        'soyad': 'Hemidov',
        'yas': 30
    },
    {
        'ad': 'Memmed',
        'soyad': 'Salamov',
        'yas': 20
    },
    {
        'ad': 'Aliye',
        'soyad': 'Qurbanova',
        'yas': 16
    },
    {
        'ad': 'Sahil',
        'soyad': 'Qeniyev',
        'yas': 45
    },
    {
        'ad': 'Ehmed',
        'soyad': 'Qeniyev',
        'yas': 50
    }
]
# Butun adlari yaz
for i in range(len(telebeler)):
    print(telebeler[i]['ad'])

# Yaslarin cemi
sumOfAges = 0
for i in range(len(telebeler)):
    sumOfAges += telebeler[i]['yas']
print('Yaslarin cemi:', sumOfAges)

# Adi Ehmed olanin melumatlari
for i in range(len(telebeler)):
    if (telebeler[i]['ad']) == 'Ehmed':
        print(telebeler[i])

# Adi Ehmed olan nece telebe var
count = 0
for i in range(len(telebeler)):
    if (telebeler[i]['ad']) == 'Ehmed':
        count += 1
print('Adi Ehmed olan nece telebe var: ', count)

# Function ile search etmek
def findUser(userName):
    for i in range(len(telebeler)):
        if (telebeler[i]['ad']) == userName:
            return telebeler[i]
print(findUser('Sahil'))

# Yas ortalamasinin ustunde olan telebeler
averageAge = sumOfAges//len(telebeler)
print('Yas ortalamasi:', averageAge)
for i in range(len(telebeler)):
    if telebeler[i]['yas'] > averageAge:
        print(telebeler[i])

# Soyadlari eyni olanlardan en yaslisi
for i in range(len(telebeler)):
    for j in range(i+1, len(telebeler)):
        if telebeler[i]['soyad'] == telebeler[j]['soyad']:
            if telebeler[i]['yas'] > telebeler[j]['yas']:
                print('Soyadlari eyni olanlardan en yaslisi:',
                      telebeler[i]['ad'])
            else:
                print('Soyadlari eyni olanlardan en yaslisi:',
                      telebeler[j]['ad'])
