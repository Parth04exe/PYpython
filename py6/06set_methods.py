# Creating some sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. add() - Adds an element to the set
a.add(7)
print("After add():", a)  # Output: {1, 2, 3, 4, 7}

# 2. update() - Adds multiple elements to the set
a.update([8, 9], [10, 11],{12,13})
print("After update():", a)  # Output: {1, 2, 3, 4, 7, 8, 9, 10, 11}

a.update([14])
print(a)
# 3. remove() - Removes a specific element
a.remove(7)
print("After remove():", a)  # Output: {1, 2, 3, 4, 8, 9, 10, 11}

# a.remove(15)
# print(a)# 12 doesn't exist, so  error

# 4. discard() - Removes an element if it exists, does nothing if it doesn't
a.discard(15)  # 12 doesn't exist, so no error
print("After discard():", a)  # Output: {1, 2, 3, 4, 8, 9, 10, 11}

# 5. pop() - Removes and returns a random element
popped_element = a.pop()
print("After pop():", a, "Popped element:", popped_element)

# 6. clear() - Clears all elements from the set
a.clear()
print("After clear():", a)  # Output: set()

# Recreating sets for further methods
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 7. union() - Returns a new set with all elements from both sets
union_set = a.union(b)
print("Union of sets:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# 8. intersection() - Returns common elements
intersection_set = a.intersection(b)
print("Intersection of sets:", intersection_set)  # Output: {3, 4}

# 9. difference() - Elements in a but not in b
difference_set = a.difference(b)
print("Difference of sets (a - b):", difference_set)  # Output: {1, 2}

# 10. symmetric_difference() - Elements in either a or b, but not both
symmetric_difference_set = a.symmetric_difference(b)
print("Symmetric Difference of sets:", symmetric_difference_set)  # Output: {1, 2, 5, 6}

# 11. isdisjoint() - Checks if sets have no common elements
print("Are sets a and b disjoint?", a.isdisjoint(b))  # Output: False

# 12. issubset() - Checks if a is a subset of b
print("Is a a subset of b?", a.issubset(b))  # Output: False
c={1,2}
print(c.issubset(a))

# 13. issuperset() - Checks if a is a superset of b
print("Is a a superset of b?", a.issuperset(b))  # Output: False
print(a.issuperset(c))
