s = input("s = ")
t = input("t = ")

dh = 0 # Hamming distance

for i in range(len(s)):
  if(s[i] != t[i]):
    dh += 1

print(dh)
