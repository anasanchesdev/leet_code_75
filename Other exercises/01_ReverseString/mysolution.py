class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


a = ['h', 'e', 'l', 'l', 'o']
exe = Solution()
exe.reverseString(a)
print(a)
