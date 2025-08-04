list1=[]
list1=input("Enter the element of the list :").split()
print("list is :",list1)

print("list operations :")
print("first element of list :",list1[0])
print("last element of list :",list1[-1])
print("first three element of list :",list1[0:3])
print("reverse element of list :",list1[::-1])

list1.append(input("enter new element to add in list:"))
print("list after adding new element :",list1)

list1.insert(int(input("enter postion of new element:")),input("enter new element to insert in list:"))
print("list after inserting new element :",list1)

list1.remove(input("enter element to remove:"))
print("list after removing element :",list1)
