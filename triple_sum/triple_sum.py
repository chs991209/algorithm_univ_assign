class TripleSum:
    def __init__(self):
        self.nums = []

    def set_nums(self, nums):
        """Set the input list of numbers."""
        self.nums = nums

    def get_nums(self):
        """Get the current list of numbers."""
        return self.nums

    def triple_sum(self):
        """Find all unique triplets in the list that sum to zero. 3 - sum triplets for the input list X"""
        if len(self.nums) < 3:
            return []

        self.nums.sort()
        result = []

        for i in range(len(self.nums) - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue

            left, right = i + 1, len(self.nums) - 1
            while left < right:
                total = self.nums[i] + self.nums[left] + self.nums[right]
                if total == 0:
                    result.append([self.nums[i], self.nums[left], self.nums[right]])

                    # Move pointers and skip duplicates
                    while left < right and self.nums[left] == self.nums[left + 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
