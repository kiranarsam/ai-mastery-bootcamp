import re

text = "Contact me at 123-456-7890"

# findall()
digits = re.findall(r"\d+", text) # + indicates more than 1 (once)

print(digits)

# sub()
updated_text = re.sub(r"\d", "X", text)
print(updated_text)
