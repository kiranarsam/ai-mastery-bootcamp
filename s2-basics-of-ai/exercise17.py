with open("sample.txt", "w") as file:
  file.write("Hello, World!")

# to open a file
with open("sample.txt", "r") as file:
  content = file.read()
  print(content)

# File is automatically closed

try:
  with open("sample1.txt", "r") as file:
    content = file.read()
except FileNotFoundError as e:
  print(f"Error {e}")
