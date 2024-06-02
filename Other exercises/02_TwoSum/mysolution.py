"""
Variáveis:
- Lista de números -> nums (list)
- Número alvo -> target (int)
- Resultado -> indexes (list)
-

Processamento das variáveis:
- Iterar sobre a nums para descobrir quais números somam e resultam em target
- Pegar o índice desses números e colocar em uma lista "indexes" ordenadamente

Restrições:
- Cada nums terá somente um resultado possível
- Não se pode usar o mesmo elemento (índice; o número em si pode repetir) duas vezes

Resultado esperado:
- Lista com os índices dos números que somam target

Passos:
1 - Definir variáveis p1 e p2 (posição 1, posição 2)
    p1 equivale ao índice do número que será comparado com p2, que acresce 1 a cada iteração
    valores iniciais: 0, 0
2 - Definir variável length que é igual ao tamanho de nums que determinará o fim da iteração
3 - Enquanto a posição 1 estiver dentro do alcance da lista, continue o código
4 - Se a posição 2 for igual ao tamanho da lista, significa que o número de p1 já foi verificado com todos os outros
elementos da lista
5 - passa para o próximo elemento da lista
6 - p2 é resetado para reiniciar a verificação
7 - Se p1 e p2 são diferentes e a soma dos seus núemros é igual ao número alvo, retorna a lista contendo p1 e p2
8 - Senão, passa p2 para o próximo número e recomeça a comparação
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        p1 = 0  # position 1
        p2 = 0  # position 2
        le = len(nums)  # tamanho da lista
        while p1 < le:
            if p2 == le:
                p1 += 1
                p2 = 0
            if p1 != p2 and nums[p1] + nums[p2] == target:
                return [p1, p2]
            p2 += 1


a = [3, 3]
exe = Solution()
print(exe.twoSum(nums=a, target=6))
