T = int(input())

for z in range(T):
  a = set(input())#unorder , unique list pr string. Unique, {1,2,3,4,3,2} set= {1,2,3,4}
  b = set(input())
  if not a&b:
    print('No')
  else:
    print('Yes')
