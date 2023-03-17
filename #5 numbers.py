def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
 
# Example usage:
nums = [3, 5, 2, 1]
missing_number = find_missing_number(nums)
print("The missing number is:", missing_number)
