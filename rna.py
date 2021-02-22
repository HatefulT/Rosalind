t = input("t (DNA) = ")
u = ""

for i in t:
  if(i == "T"):
    u += "U"
  else:
    u += i

print("RNA = "+u)
