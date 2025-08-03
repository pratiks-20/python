n=int(input("Enter the number: "))

squareRoot=0
for i in range(1,n+1):
    if i*i==n:
        squareRoot=i
        break

if squareRoot == 0:
    print("The square root is not a perfect square")
else:
    print("Square root:",squareRoot);
    prime=True
    if squareRoot < 2:
        prime=False
    else:
        for i in range(2,squareRoot):
            if squareRoot % i == 0:
                prime=False
                break

print("prime"if prime else"not prime")
