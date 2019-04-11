n,x= map(int, input().split())
a= list(map(int, input().split()))
for i in range(x):
    min = i
    for j in range(i+1, n):
        if(a[j]< a[min]):
            min=j
    a[i],a[min]= a[min],a[i]
    
for i in range(n):
    print("%d" %a[i], end=" ")
    
        
