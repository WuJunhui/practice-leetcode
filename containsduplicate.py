class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) ==len(nums)
        
if __name__=='__main__':
    nums=[]
    a=Solution()
    print a.containsDuplicate(nums)