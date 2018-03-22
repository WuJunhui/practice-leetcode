class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #for i in range(k):
        #    nums[:]=nums[-1:]+nums[:-1]

        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        
if __name__=='__main__':
    nums=[1,2,3,4,5,6,7,8]
    k = 3 
    a=Solution()
    a.rotate(nums,k)
    print nums