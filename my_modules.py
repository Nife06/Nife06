def count_vowels(text):
    """Return the number of vowels in the given text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def add_numbers(a, b):
    return a + b
