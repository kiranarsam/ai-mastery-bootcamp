# os module
import os

print(os.getcwd())

if os.path.exists("test_dir") is None:
  os.mkdir("test_dir")
else:
  print("test_dir already exists")

if os.path.exists(os.path.join("test_dir", "file.txt")):
  os.remove("test_dir/file.txt")
else:
  print("File not found")
