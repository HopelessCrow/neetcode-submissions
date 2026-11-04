class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ""
        for char in s:
            reverse = char + reverse
        s=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reverse=re.sub(r'[^a-zA-Z0-9]', '', reverse).lower()
        print(s)
        print (reverse)
        return reverse==s
        