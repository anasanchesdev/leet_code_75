# from stackoverflow
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        #  0  1  2  3
        # [1, 2, 3, 3] = 4
        # tamanho da lista original
        nums_length = len(nums)

        # cria uma lista com mesmo tamanho de nums, só que com todos os elementos iguais a 1
        unit_list = [1] * nums_length

        # reversed -> contagem inversa
        # para cada index da lista unitária, começando do último index até o primeiro...
        for index in range(nums_length - 2, -1, -1):  # ou reversed(range(nums_length - 1)) para inverter o range

            # cada elemento da lista unitária é igual ao próximo vezes o próximo elemento da lista original
            # em ordem decrescente
            unit_list[index] = unit_list[index + 1] * nums[index + 1]

        # repare que apenas o primeiro e segundo itens foram multiplicados
        print(unit_list)
        product = 1  # acumulador de produtos
        print(f'original: {nums}\nunitária: {unit_list}')
        print(unit_list)

        for index in range(nums_length):
            # nº da lista original correspondente ao index da iteração
            num_from_index = nums[index]
            print(index, num_from_index)

            # modifica este nº pelo produto (inicialmente 1) vezes o nº da lista unitária de index equivalente
            nums[index] = product * unit_list[index]
            print(nums)

            # o produto é multiplicado pelo nº da iteração atual da lista original -> se torna cumulativo
            product *= num_from_index
            print(f'produto: {product}')
        return nums


lista = [5, 4, 5, 4]
exe = Solution()
print(exe.productExceptSelf(lista))
