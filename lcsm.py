f = open("rosalind_lcsm.txt", "r")
s1 = f.readlines()
ss = []
tmp = None
for i in s1:
  if(i.startswith(">")):
    if(tmp):
      ss.append(tmp)
    tmp = ""
  else:
    tmp += i.strip()
f.close()

alph = ["A", "T", "C", "G"]

def check(substring, strings):
  found = True
  for s in strings:
    if(s.find(substring) == -1):
      found = False
      break
  return found

def getLongestStartingWith(starts, strings):
  maxStr = starts
  for l in alph:
    s1 = starts + l
    if(check(s1, strings)):
      s1 = getLongestStartingWith(s1, strings)
      if(len(s1) > len(maxStr)):
        maxStr = s1

  return maxStr

print(getLongestStartingWith("", ss))







