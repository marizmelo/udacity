def small_words(words):
  for word in words:
    if len(word) <= 3:
      yield word

print [w for w in small_words(["The", "quick", "brown", "fox"])]   
   