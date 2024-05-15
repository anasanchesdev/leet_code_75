# RUNTIME: 39ms (beats 40.36%)  MEMORY: 16.69MB (beats 79.91%)
# [ Time taken: 8 m 22 s ]
class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        n.reverse()
        w = ' '.join(n)
        return w
