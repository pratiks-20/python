
a=set(input("enter the elements of the set: "))
print(a)
print(type(a))

a.add(9)
print("set after new element added : ",a)

a.remove("r")
print("set after an element is removed : ",a)

a.discard("t")
print("set after an element is discarded : ",a)

a.pop()
print("set after an element is pop : ",a)

a.clear()
print(a)

m=set(input("enter the elements of the set1: "))
n=set(input("enter the elements of the set2: "))

print(m.union(n))
print(m.intersection(n))
print(m.difference(n))
print(m.issubset(n))
print(m.issuperset(n))