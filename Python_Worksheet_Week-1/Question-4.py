def is_palindrome(text):
    lowercase_text = text.lower()
    cleaned_text = lowercase_text.replace(" ", "")

    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False


print(is_palindrome("level"))
print(is_palindrome("Hello"))
print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))