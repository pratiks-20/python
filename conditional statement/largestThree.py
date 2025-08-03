num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))

if (num1 > num2 and num1>num3):
    print(num1,"is a greater number than",num2,"and",num3)

elif (num2 > num1 and num2 > num3):
    print(num2,"is a greater number than",num1,"and",num3)
else:
    print(num3,"is greater number than",num1,"and",num2)