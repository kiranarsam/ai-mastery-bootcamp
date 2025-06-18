
num = int(input("Enter a number: "))
sqroot_num = int(num ** 0.5)
print("sqroot_num = ", sqroot_num)
print("sqroot_num + 1 = ", sqroot_num + 1)

if num > 1:
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      print(f"{num} is not a prime number")
      break
  else:
    print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")
