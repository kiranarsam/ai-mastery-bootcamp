sentence = input("Enter a Sentence: ")

# split the sentence
words = sentence.split()

# empty dictionary
word_count = {}

# count word frequencies
for word in words:
  word = word.lower()
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)
