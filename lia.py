k = int(input("k = "))
n = int(input("n = "))

e = 2**k

def C(a, b):
  out = 1
  for i in range(b, b-a, -1):
    out *= i
  for i in range(1, a+1):
    out /= i
  return out

pr = 0

for i in range(n, e+1):
  pr += C(i, e) * 0.25**i * 0.75**(e-i)
  print(i, e)

print(pr)
