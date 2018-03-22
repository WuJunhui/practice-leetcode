class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1

        nums[:]=sorted(dic.keys())
        return len(nums)
