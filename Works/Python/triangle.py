arr=[]
for i in range(0, 5):
    for j in range(0,5):
        if i+j>=4:
            arr[i][j]='*'

for i in range(0, 5):
    for j in range(0,5):
        print(arr[i][j],end='')
    print()