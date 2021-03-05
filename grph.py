k = 3
s = []
rawInput = open("rosalind_grph.txt", "r").readlines()
tmp = None
index = 0
for line in rawInput:
  if(line.startswith(">")):
    if(tmp):
      s[index][1] = tmp[:k]
      s[index][2] = tmp[len(tmp)-k:]
      index += 1
    name = line[1:].strip()
    tmp = ""
    s.append([name, "", ""])
  else:
    tmp += line.strip()
if(name):
  s[index][1] = tmp[:k]
  s[index][2] = tmp[len(tmp)-k:]

edges = []

for i in range(len(s)-1):
  for j in range(i+1, len(s)):
    if(s[i][1] == s[j][2]):
      edges.append(s[j][0] +" "+s[i][0])
    elif(s[i][2] == s[j][1]):
      edges.append(s[i][0] +" "+s[j][0])

#print(edges)

for i in edges:
  print(i)
