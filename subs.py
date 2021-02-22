s = input("s = ")
t = input("t = ")

positions = []

for i in range(len(s)-len(t)+1):
  tmp = True
  for j in range(len(t)):
    if(s[i+j] != t[j]):
      tmp = False
      break
  if(tmp):
    positions.append(i+1)

for i in positions:
  print(i)
