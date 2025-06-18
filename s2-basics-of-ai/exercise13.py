first = "hello"
second = "World"

result = first + " " + second
print(result)

text = "Python Programming"
print(text[0:6])
print(text[-11:])

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")


# split()

sentence = "Python is fun"
words = sentence.split()
print(words)

# join()
new_sentence = "|".join(words)
print(new_sentence)

# replace()
text = "I love Python. I hate coding."
updated_text = text.replace("Python", "python programming")
print(updated_text)

# strip()
messy = "      Hello, World      "
cleaned_text = messy.strip()
print(cleaned_text)
