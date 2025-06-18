
numbers = [1, 2, 3, 4]

fruits = ["apple", "banana", "cherry"]

mixed = [1, "apple", True]

print(numbers[2])
print(fruits[2])
print(mixed[1])

# negative indexing
print(fruits[-1])

# add items
fruits.append("orange")
fruits.insert(1, "grapes")

print(fruits)

# removing an element
fruits.remove("banana")

# delete an element
del fruits[0]

# removes the last element from the list
fruits.pop()

fruits.pop()

print(fruits)

fruits = ["apple", "banana", "cherry", "orange"]

# slices
print("Doing slice operations ")
print(fruits)
sliced_fruits = fruits[2:4]
print(sliced_fruits)

# tuples

colors = ("red", "green", "blue")

single_item = ("glass",)
print(colors)
print(single_item)

print(colors[0])
print(colors[-1])


# dictionaries
student = {
  "name" : "Alice",
  "age" : 25,
  "grade" : "A"
}

print(student)
print(student["age"])

# add
student["subject"] = "Math"
student["age"] = 32

print(student)

del student["grade"]
print(student)

student.pop("subject")
print(student)

# key value

for key, value in student.items():
  print(key, value)


# Sets
numbers = {1, 2, 3, 4, 5}
empty_set = {}
print(numbers)
numbers.add(8)
print(numbers)
numbers.remove(2)
print(numbers)

set1 = {1,2,3}
set2 = {3,4,5}

# union
print(set1 | set2)
# intersection
print(set1 & set2)
# difference
print(set1 - set2)
