s = input("s =")

table1 = "UUU F,CUU L,AUU I,GUU V,UUC F,CUC L,AUC I,GUC V,UUA L,CUA L,AUA I,GUA V,UUG L,CUG L,AUG M,GUG V,UCU S,CCU P,ACU T,GCU A,UCC S,CCC P,ACC T,GCC A,UCA S,CCA P,ACA T,GCA A,UCG S,CCG P,ACG T,GCG A,UAU Y,CAU H,AAU N,GAU D,UAC Y,CAC H,AAC N,GAC D,UAA Stop,CAA Q,AAA K,GAA E,UAG Stop,CAG Q,AAG K,GAG E,UGU C,CGU R,AGU S,GGU G,UGC C,CGC R,AGC S,GGC G,UGA Stop,CGA R,AGA R,GGA G,UGG W,CGG R,AGG R,GGG G".split(",")
table = {}
for i in table1:
  i1 = i.split(" ")
  table[i1[0]] = i1[1]

protein = ""

for i in range(len(s)//3):
  s1 = s[3*i:3*i+3:]
  if(table[s1] != "Stop"):
    protein += table[s1]
  else:
    break

print(protein)
