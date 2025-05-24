def add_numbera(a,b):
  return a+b

def count_vowels(text):
  '''Return the number of vowels in a given text.'''
  vowels = "aeiouAEIOU"
  return sum(i for char in text if char in vowels)

