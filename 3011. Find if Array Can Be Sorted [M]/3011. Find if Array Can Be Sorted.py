class Solution:
    def canSortArray(self, nums) -> bool:
        prev_max = 0
        this_max = 0
        bit_count = -1
        for num in nums:
            # num.bit_count() returns the number of set bits in num
            this_bit_count = num.bit_count()
            # if the number of set bits is not equal to the current bit_count
            if this_bit_count != bit_count:
                prev_max = this_max
                this_max = 0
                bit_count = this_bit_count

            # return False if the previous max is greater than the current number
            if prev_max > num:
                return False

            # this_max stores the maximum number of set bits in the current segment
            this_max = max(this_max, num)
        return True

# test
solution = Solution()
print(solution.canSortArray([8,4,2,30,15]))
print(solution.canSortArray([1,2,3,4,5]))
print(solution.canSortArray([3,16,8,4,2]))