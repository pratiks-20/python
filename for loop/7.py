n=49

for i in range (n):
    if i*i==n:
        squareroot = i
        break

if squareroot<2:
    print("squareroot ofnumber is not prime")
else:
    print("squareroot : ",squareroot)
    prime =True
    for i in range(2,squareroot):
        if squareroot % i==0:
            prime=False
            break

print("prime"if prime else"not prime")

