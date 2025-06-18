person = {
  "name" : "Alice",
  "age" : 25,
  "grade" : "A"
}

print(person)

person["address"] = "123 Main St"

person["age"] = 32

if "grade" in person:
  del person["grade"]

print(person)
