x = float(input("Enter value of x (in radians): "))
n = int(input("Enter maximum power (even number): "))

cosx = 0
sign = 1

for i in range(0, n + 1, 2):  # 0, 2, 4, ..., n
    fact = 1
    for j in range(1, i + 1):  # calculating factorial of i
        fact = fact * j
    term = (x**i) / fact
    cosx = cosx + sign * term
    sign = -sign  # alternate the sign

print("Cos(x) ≈", cosx)
