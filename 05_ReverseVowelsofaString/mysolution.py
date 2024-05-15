# RUNTIME: 55ms (beats 43.06%)  MEMORY: 17.22MB (beats 90.84%)
# [ Time taken: 10 m 54 s ]
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vl = []
        ns = ''
        c = 0
        for l in s:
            if l in v:
                vl.append(l)
        vl.reverse()
        for l in s:
            if l in v:
                ns += vl[c]
                c += 1
            else:
                ns += l
        return ns
