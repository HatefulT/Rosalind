s1 = None
s = ""
while s1 != "":
  s1 = input().replace("\n", "")
  s += s1

table = {
  "A": "T",
  "T": "A",
  "G": "C",
  "C": "G"
}

for i in range(len(s)-4+1):
  for j in range(4, min(12+1, len(s)-i+1), 2):
    found = True
    for k in range(int(j/2)):
      if(s[i+k] != table[s[i+j-k-1]]):
        found = False
        break
    if(found):
      print(i+1, j)
#      print(s[i:i+j:])
