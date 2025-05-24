def count_vowels(text):
  '''Returns the number of vowels in the given text'''
  vowels = "aeiouAEIOU"
  return sum(i for char in text if char in vowels)

def add_numbers(a,b):
  return a+b

def reverse_text(text):
  return text[::-1]
