def is_palindrome(text):
  text = "".join(char.lower() for char in text if char.isalnum())

  # syntax: to reverse string text[start:stop:step]
  return text == text[::-1] # [::-1] is used for reverse the text

input_text = input("Enter a text to valid palindrome: ")

if is_palindrome(input_text):
  print(f"{input_text} is a palindrome")
else:
  print(f"{input_text} is not a palindrome")
