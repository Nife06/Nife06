def is_palindrome(word):
    """Return True if the word is a palindrome, False otherwise."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def reverse_text(text):
    return text[::-1]
