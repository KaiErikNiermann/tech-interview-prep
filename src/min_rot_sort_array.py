class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        ### Thought process
        - The key insight here is that the minimum element is the only element in the array that is smaller than its previous element.
        - Since we want to solve the problem in log n the first intuition is always divide and conquer, in this instance that takes the form of a binary search
        - Two key things to remember, we init left and right to `0` and `len(nums) - 1`, and the mid point is calculated as `left + (right - left) // 2`

        ### Notes
        - time complexity is $O(log n)$
        - space complexity is $O(1)$
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMinRecursive(self, nums: list[int]) -> int:
        """
        ### Thought process
        - Similar to the iterative approach, just using recursion
        - The base case is when left >= right, we return the element at the left index
        - Probably worse for interviews, but good to know

        ### Notes
        - time complexity is $O(log n)$
        - space complexity is $O(log n)$ due to the recursive stack
        """

        def helper(left, right):
            if left >= right:
                return nums[left]
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                return helper(mid + 1, right)
            else:
                return helper(left, mid)

        return helper(0, len(nums) - 1)
