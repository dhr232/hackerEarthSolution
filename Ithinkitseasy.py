# Write your code here
for _ in range(int(input())):
    arr = list(map(str, input().split()))
    arr.sort(key=len)
    print(end=' ')
    for v in arr:
        print(v,end=' ')
    print()
