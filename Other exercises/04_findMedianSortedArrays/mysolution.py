class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # juntar as duas listas em nums1
        for n in nums2:
            nums1.append(n)

        # ordenar lista
        nums1.sort()

        # tamanho de nums1
        le = len(nums1)

        # elemento central
        ce = le / 2

        # checar se é par ou ímpar
        if le % 2 == 0:

            # pegar números do meio e fazer média
            result = (nums1[int(ce)] + nums1[int(ce - 1)]) / 2
            return result
        return ce.__ceil__()


n1 = [2]
n2 = []
exe = Solution()
print(exe.findMedianSortedArrays(n1, n2))
