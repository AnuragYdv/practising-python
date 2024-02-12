arr=[10,20,20,10,10,30,50,10,20]
n=9
for i in range(0,n):
    counter=0
    for j in range(0,n):
        print(counter)
        if arr[i]==arr[j]:
            counter+=1