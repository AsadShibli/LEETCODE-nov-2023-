class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for i in arr:
            pre = min(pre+1,i)
        return pre
