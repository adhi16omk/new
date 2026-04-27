def remove_duplicates(nums):
    if not nums:
        return 0

    # Pointer for the position of unique elements
    j = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    # New length is j + 1
    return j + 1


# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)

print("New length:", new_length)
print("Updated list:", nums[:new_length])
