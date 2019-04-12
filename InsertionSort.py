n= int(input())
a= list(map(int, input().split()))
for i in range(n):
    min =i
    for j in range(i+1, n):
        if(a[j]< a[min]):
            min=j
    a[i],a[min]=a[min],a[i]
    
sum1=0
for i in range(len(a)):
    
    if(a[i]%2==0):
        sum1+=a[i]
        print(a[i],end=" ")
print(sum1, end=" ")
sum2=0
for i in range(len(a)):
    
    if(a[i]%2!=0):
        sum2+=a[i]
        print(a[i],end=" ")
print(sum2, end=" ")
