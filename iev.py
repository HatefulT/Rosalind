n = [int(i) for i in input().split(" ")]

# AA-AA - 100%
# AA-Aa - 100%
# AA-aa - 100%
# Aa-Aa - 75%
# Aa-aa - 50%
# aa-aa - 0%

print( 2*n[0] + 2*n[1] + 2*n[2] + 2*n[3]*0.75 + 2*n[4]*0.50 )
