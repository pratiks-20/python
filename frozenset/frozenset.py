a = frozenset(input("enter a first frozenset : "))
b = frozenset(input("enter a second frozenset : "))


print("union of two frozensets is : ",a.union(b))
print("intersection of two frozensets is : ",a.intersection(b))
print("differece of two frozensets is : ",a.difference(b))
print("first frozenset is subset of second set : ",a.issubset(b))
print("first frozenset is superset of second set : ",a.issuperset(b))