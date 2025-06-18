
def count_words_and_lines(filename):
  try:
    with open(filename, "r") as file:
      lines = file.readlines()
      line_count = len(lines)
      result = []
      for line in lines:
        result.append(len(line.split()))
      word_count = sum(result)

      print(f"Number of lines: {line_count}")
      print(f"Number of words: {word_count}")
  except FileNotFoundError as e:
    print(f"File {filename} not found. {e}")


# Invoke the func call
count_words_and_lines("sample.txt")
