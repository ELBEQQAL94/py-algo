def reverse_words(text):
  words = text.split(" ")
  result = []
  for word in words:
      result.append(word[::-1])
  return " ".join(result)


# print(reverse_words('apple'))
# , 'elppa')

print(reverse_words('double  spaced  words'))
# , 'elbuod  decaps  sdrow')