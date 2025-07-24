"""
Here’s a useful list of the most common methods you’ll actually use:

Adding & Removing
append(x) – Adds an item x to the end of the list.
extend(iterable) – Appends all elements of an iterable (e.g., another list).
insert(i, x) – Inserts an item x at position i.
remove(x) – Removes the first occurrence of item x.
pop([i]) – Removes and returns the item at position i (default: last).
clear() – Removes all items from the list.
Searching & Counting
index(x[, start[, end]]) – Returns the index of the first occurrence of x.
count(x) – Returns how many times x appears.
Sorting & Reversing
sort(key=None, reverse=False) – Sorts the list in-place.
reverse() – Reverses the list in-place.
Copying
copy() – Returns a shallow copy of the list."""

# Create a list of two strings
l = ["raj", "ravi"]

# Print the entire list
print(l)          # Output: ['raj', 'ravi']

# Print the first element (index 0)
print(l[0])       # Output: raj

# Change the second element (index 1) to "rani"
l[1] = "rani"
print(l)          # Output: ['raj', 'rani']

# Print the updated list
print(l)          # Output: ['raj', 'rani']

# Append a new element "raviraj" to the end of the list
l.append("raviraj")
print(l)          # Output: ['raj', 'rani', 'raviraj']

# Append "raviraj" again to the list (duplicates allowed)
l.append("raviraj")
print(l)          # Output: ['raj', 'rani', 'raviraj', 'raviraj','raviraj']
l.append("raviraj")
print(l.index("raviraj"))
print(l.count("raviraj"))
l.insert(0,"vani")
print(l) 
l.sort()
print(l)
l.reverse()
print(l)
l.pop(0)
print(l)
l.append("vani")
print(l)
l.remove("vani")
print(l)
l.append("vani")
print(l)
print(l.count("raviraj"))
lst = [1, 2, 3, 2]
print(lst)
lst.remove(2)    # Removes the first 2
print(lst)
lst.append(2)
print(lst)
lst.pop(1)
print(lst)
print(lst.count(2))
print(lst[::-1])