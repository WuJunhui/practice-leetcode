class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in nums[1:]:
            result ^=i
        return result


if __name__=='__main__':
    nums=[3,1,2,1,2]
    a=Solution()
    print a.singleNumber(nums)