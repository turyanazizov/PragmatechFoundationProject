testler=[
    {'sual':'HTML texnologiyasinin temeli necenci ilde qoyulub?',
    'cavablar':[1995,1978,1990,1967],
    'cavab':'A'},
    {'sual':'Hansi Backend texnologiyasi deyil?',
    'cavablar':['C#','Python','CSS','PHP'],
    'cavab':'B'},
    {'sual':'Python texnologiyasinin temeli necenci ilde qoyulub?',
    'cavablar':[1992,1995,1991,1987],
    'cavab':'C'},
    {'sual':'''Python-da 5*'s' yazsaq neticede ne gorerik?''',
    'cavablar':['sssss','Error','5s','5'],
    'cavab':'A'},
    {'sual':'Biri HTML tagi deyil',
    'cavablar':['a','b','br','app'],
    'cavab':'D'},
]
bendler=['A','B','C','D']
bal=0
for test in testler:
    print(test['sual'])
    for i in range(len(test['cavablar'])):
        print(bendler[i],')',test['cavablar'][i])

    userinCavabi=input('Cavabinizi yazin: ')
    if userinCavabi==test['cavab']:
        print('Cavab dogrudur!')
        bal+=100//len(testler)
    else:
        print('Cavab yanlisdir!')

print(f'Sizin neticeniz: {bal}/100')