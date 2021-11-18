users=[
    {
        'ad':'Turyan1',
        'soyad':'Azizov1'
    },
    {
        'ad':'Turyan2',
        'soyad':'Azizov2'
    },
    {
        'ad':'Turyan3',
        'soyad':'Azizov3'
    }
]
print(users)
i=input('reqem yaz')
del users[int(i)]
print(users)