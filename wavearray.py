#Wave Array is a simple yet interesting problem in the domain of array manipulation.
# Given an array of integers, the task is to transform it into a 'wave' array by swapping adjacent elements.
from typing import List

class Solution:
    def convertToWave(self, array_length: int, array: List[int]) -> None:
        # Loop through the array with a step of 2 (starting from index 1)
        for i in range(1, array_length, 2):
            # Swap the current element with the next element
            array[i - 1], array[i] = array[i], array[i - 1]