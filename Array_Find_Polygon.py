t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))#to insert the array element
    m=max(l)# remove maximum frim array and check the sum of remaining
    l.remove(m)
    if(m>=sum(l)):#if true than we can make polygon out of array
        print("No")
    else:
        print("Yes")
