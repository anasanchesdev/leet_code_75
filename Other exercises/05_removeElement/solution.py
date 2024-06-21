def removeElement(nums: list[int], val: int):
    k = len([num for num in nums if num != val])
    length = len(nums)
    removed = [0] * length
    position = 0
    for index in reversed(range(length)):
        ...


print(removeElement(nums=[2, 3, 3, 2], val=2))
