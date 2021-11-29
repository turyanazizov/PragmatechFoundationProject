string=input()
isdigit=False
isalnum=False
isalpha=False
isupper=False
islower=False

for char in string:
    if char.isalnum()==True:
        isalnum=True
    if char.isalpha()==True:
        isalpha=True
    if char.isdigit()==True:
        isdigit=True
    if char.islower()==True:
        islower=True
    if char.isupper()==True:
        isupper=True

print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper)
