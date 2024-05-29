class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        answer = [number for number in nums]
        mult = 1

        for index1, num1 in enumerate(nums):

            for index2, num2 in enumerate(nums):
                print(f'index 1: {index1} index 2: {index2}')
                if index1 == index2:
                    continue
                mult *= num2

            answer[index1] = mult
            mult = 1

        return answer


lista = [0, 0]
exe = Solution()
print(exe.productExceptSelf(lista))
