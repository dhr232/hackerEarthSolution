for _ in  range(int(input())):
    string,n, m=input().split(" ")
    n=int(n)
    m= int(m)
    print(string[:n]+''.join(sorted(string[n:m+1], reverse= True))+string[m+1:])
