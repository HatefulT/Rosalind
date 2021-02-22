k = int(input("k =")) # AA
m = int(input("m =")) # Aa
n = int(input("n =")) # aa

# let C(n, k) be the number of combinations from n to k C(n, k) = k!/(n! * (k-n)!)

# k-k: AA          (100%) C(2, k) = k*(k-1)/2
# k-m: AA AA Aa Aa (100%) k*m
# k-n: Aa Aa Aa Aa (100%) k*n
# m-m: AA Aa Aa aa (75%)  C(2, k) = m*(m-1)/2
# m-n: Aa Aa aa aa (50%)  m*n
# n-n: aa          (0%)   C(2, k) = n*(n-1)/2

# Probability = desired / total
# total = C(2, k+m+n) = (k+m+n)*(k+m+n-1)/2

total = (k+m+n)*(k+m+n-1)/2

print(str( (k*(k-1)/2+k*m+k*n+.75*m*(m-1)/2+0.5*m*n)/total ))




