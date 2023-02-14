# =========================== 8 kyu Is It a Palindrome? ===========================
def is_palindrome(s):
    
    return s.lower() == s[::-1].lower()

print(is_palindrome("Madam"))
print(is_palindrome("121"))
print(is_palindrome("yehya"))