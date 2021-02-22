s1 = input("s1 = ")
s2 = input("s2 = ")
s3 = input("s3 = ")

'''
In practice, the GC-content of most eukaryotic genomes hovers around 50%. However, because genomes are so long, we may be able to distinguish species based on very small discrepancies in GC-content; furthermore, most prokaryotes have a GC-content significantly higher than 50%, so that GC-content can be used to quickly differentiate many prokaryotes and eukaryotes by using relatively small DNA samples.
'''

gc1 = 0
gc2 = 0
gc3 = 0

for i in s1:
  if(i == "G" or i == "C"):
    gc1 += 1
for i in s2:
  if(i == "G" or i == "C"):
    gc2 += 1
for i in s3:
  if(i == "G" or i == "C"):
    gc3 += 1

if(gc1 > gc2 and gc1 > gc3):
  print("gc1 =", str(gc1*100/len(s1)))
elif(gc2 > gc1 and gc2 > gc3):
  print("gc2 =", str(gc2*100/len(s2)))
elif(gc3 > gc1 and gc3 > gc2):
  print("gc3 =", str(gc3*100/len(s3)))
