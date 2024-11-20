class Solution(object):
    def twoSum(self, nums, target):
        size_nums = len(nums)
        for i in range (size_nums):
            for j in range (i + 1, size_nums):
                if nums[i] != nums[j]:
                    if nums[i] + nums[j] == target:
                        return [i, j]
    

def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    returno = solution.twoSum(nums=nums, target=target)
    print(returno)

    # if index a[x] + index a[y] = target
    # return list [x, y]

if __name__ == '__main__':
    main()