s = input("s = ")[::-1]

revc = {
  "A": "T",
  "T": "A",
  "G": "C",
  "C": "G"
}

sc = ""

for i in s:
  sc += revc[i]

print("sc =", sc)
