try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)

except ValueError:
    print("Oops! That's not a valid number.")

except ZeroDivisionError:
    print("You can't divide by zero!")
    
finally:
    print("Program ended.")