# example 1 control flow
num = 2
if num > 0:
  print("Positive Number")
elif num == 0:
  print("Zero")
else:
  print("Negative Number")

# example2
age = 25
if age > 18:
  if age < 30:
    print("Young Adult")
  else:
    print("Adult")
else:
  print("Young")

#Syntax for for-loop
# for item in sequence:
#   #code block

# Loop through list of items
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)

# Loop with range
for i in range(5): # [0,1,2,3,4]
  print(i)

# Count down from 5
count = 5
while count > 0:
  print(count)
  count -= 1

print("Outside while loop")


for i in range(10):
  if i == 5:
    break
  print(i)

print("Outside for break loop")

for i in range(10):
  if i == 5:
    continue
  print(i)

print("Outside for continue loop")

# print even numbers
for i in range(10):
  if i % 2 != 0 :
    continue
  print(i)

print("Outside for odd loop")
