n = int(input())

def perms(n):
  o = 1
  for i in range(1, n+1):
    o *= i
  return o

def createPerms(start, chosen, n):
  if(len(start) == n):
    s = ""
    for i in start:
      s += str(i) + " "
    print(s)
    return
  for i in range(len(chosen)):
    if(not chosen[i]):
      newChosen = []
      newStart = []
      for j in range(n):
        if(i == j):
          newChosen.append(True)
        else:
          newChosen.append(chosen[j])
      for j in range(len(start)):
        newStart.append(start[j])
      newStart.append(i+1)
      createPerms(newStart, newChosen, n)

print(perms(n))

chosen1 = []
for i in range(n):
  chosen1.append(False)
createPerms([], chosen1, n)
