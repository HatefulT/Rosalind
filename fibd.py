n = int(input("n = "))
m = int(input("m = "))

a = 1
b = []

for i in range(m-1):
  b.append(0)

for i in range(n-1):
  dA = 0
  for j in b:
    dA += j
  for j in range(len(b)-1, 0, -1):
    b[j] = b[j-1]
  b[0] = a
  a = dA
  
  total = a
  for j in b:
    total += j
  print(total)
