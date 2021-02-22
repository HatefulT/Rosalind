s = input("s = ")

NA = 0
NC = 0
NG = 0
NT = 0

for i in s:
  if(i == "A"):
    NA += 1
  elif(i == "C"):
    NC += 1
  elif(i == "G"):
    NG += 1   
  elif(i == "T"):
    NT += 1

print(NA, NC, NG, NT)



