"""return the sum of elements in a special array which might aslo conatin many arrays in arrays. 
ex-n an array, [x, y], the product sum is (x + y).
In array [x, [y, z]], the product sum is x + 2 * (y + z). In array [x, [y, [z]]], 
the product sum is x + 2 * (y + 3z)"""

def productsum(nums, multiplier = 1):
    sum = 0
    for i in range(len(nums)):
        if isinstance(nums[i], list):
            sum += productsum(nums[i],multiplier+1)*multiplier
        else:
            sum += nums[i]*multiplier

    return sum

nums = [1, 2, [1,2,3]]
print(productsum(nums))
        