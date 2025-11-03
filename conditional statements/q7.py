n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))


if n1<n2 and n1<n3:
    print("first number is smallest")
elif n2<n1 and n2<n3:
    print("second number is smallest")
else :
    print("third number is smallest")