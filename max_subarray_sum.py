def max_subarray_sum(nums):  
    if not nums:  
        return 0  
      
    max_so_far = nums[0]  
    curr_max = nums[0]  
  
    for num in nums[1:]:  
        curr_max = max(num, curr_max + num)  
        max_so_far = max(max_so_far, curr_max)  
  
    return max_so_far  
  
# 测试代码  
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
print(max_subarray_sum(nums))  