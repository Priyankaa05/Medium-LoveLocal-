def majorityElement(nums):
    if not nums:
        return []

    count1, count2, candidate1, candidate2 = 0, 0, 0, 1

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result


user_input = input("Enter the elements of the array separated by space: ")
nums = list(map(int, user_input.strip('[]').split(',')))

result = majorityElement(nums)
print("Elements that appear more than ⌊ n/3 ⌋ times:", result)
