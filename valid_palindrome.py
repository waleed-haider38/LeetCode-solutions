class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = " "
        for char in s:
            if char.isalnum():
                result += char
        result.replace(" ", "")
        reverse_s = result[::-1]
        if result == reverse_s:
            return True
        else:
            return False
        