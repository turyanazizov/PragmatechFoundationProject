n=int(input())
arr =list(map(int, input().split(" ")))
newArr=[]
arr.sort()
maxDigit=arr[n-1]

for i in range(len(arr)):
    if arr[i]!=maxDigit:
        newArr.append(arr[i])

print(newArr[len(newArr)-1])