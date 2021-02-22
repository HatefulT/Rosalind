n = int(input("n = "))
k = int(input("k = "))

# each month every pair of reproduction-age rabbits produces a litter of k rabbit pairs
# find the total number of rabbit pairs after n months if we start with 1 rabbit pair

a = 1 # small pairs
b = 0 # reproduction-age pairs

for i in range(n):
  dB = a
  a = k*b
  b += dB
  print(a, b)
print(b)
