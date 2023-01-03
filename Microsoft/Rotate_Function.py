class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = 0
        base = 0
        for idx, n in enumerate(nums):
            base += idx * n
            s += n
        ret = base
        for i in range(len(nums)-1, 0, -1):
            b = nums[i]
            base = base + s - len(nums) * b
            ret = max(ret, base)
        return ret
