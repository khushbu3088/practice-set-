#5. Write a Python program to remove an item from a set if it is present in the set.
s={3,4,5,6,7,8}
if 4 in s:
    s.remove(4)
    print(s)
    print("this item is remove from set")
else:
    print("error")
