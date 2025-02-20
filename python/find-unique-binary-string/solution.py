from typing import List
from utils import check_efficiency


class Solution:
    @check_efficiency
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        digits_number = len(nums[0])
        max_value = pow(digits_number, 2)

        for n in range(max_value + 1):
            n_str = f"{n:0{digits_number}b}"
            if n_str not in nums:
                return n_str


if __name__ == '__main__':
    Solution().findDifferentBinaryString(['000','111'])