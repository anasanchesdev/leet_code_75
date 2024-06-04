"""
OBJETIVO: maior sequência de caracteres que não se repetem
VARIÁVEIS:
- str -> s: string a ser processada
- str -> sub: substring
- int -> pos: posição de iteração
- int -> le_sub: tamanho da substring (resultado)

PROCESSAMENTO DE VARIÁVEIS:
-
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        le = len(s)
        pos = 0
        num_ite = 0
        sub = ""
        while num_ite != le:
            for letter in s:
                if letter not in sub:
                    sub += letter



        # sub = ""
        # for index, letter in enumerate(s):
        #     next = s[index + 1] if index < len(s) - 1 else letter
        #     if letter != next and letter not in sub:
        #         sub += next

        print(sub, len(sub))


exe = Solution()
print(exe.lengthOfLongestSubstring("abcabcbb"))
