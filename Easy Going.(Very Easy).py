'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t= int(input())
for g in range(t):
    n, m= list(map(int,input().split(" ")))
    # print("%d %d" %(n,m))
    a= list(map(int,input().split(" ")))
    a.sort()
    print(abs(sum(a[0:n-m])-sum(a[m:n])), end= "\n")
