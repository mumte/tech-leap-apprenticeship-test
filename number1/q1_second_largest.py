def second_largest(numbers):
    """
    This function returns the second-largest number in a given list of integers.
    """
    # Step 1: Remove duplicates
    unique_numbers = list(set(numbers))
    
    # Step 2: Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # Step 3: Return the second item
    if len(unique_numbers) < 2:
        return None  # if there is no second-largest
    return unique_numbers[1]

# Example usage
nums = [10, 20, 4, 45, 99, 99, 20]
print("Second largest number is:", second_largest(nums))
