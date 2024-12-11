def three_sums(nums, target):
    nums.sort()  # Sort the array
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l = i + 1    # left pointer
        r =  len(nums) - 1  # right pointers
        
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            
            if current_sum == target:
                result.append([nums[i], nums[l], nums[r]])
                
                # Move left pointer and avoid duplicates
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Move right pointer and avoid duplicates
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                
                # Move both pointers after finding a valid triplet
                l += 1
                r -= 1
            
            elif current_sum > target:
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1  # Move the right pointer after handling duplicates
            
            elif current_sum < target:
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                l += 1  # Move the left pointer after handling duplicates
    
    return result
