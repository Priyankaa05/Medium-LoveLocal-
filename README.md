# Medium-LoveLocal-
Q 2.Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Explaination:
majorityElement Function:

This function takes a list of integers (nums) as input and returns a list of elements that appear more than ⌊ n/3 ⌋ times in the array.
The function uses the Boyer-Moore Voting Algorithm to find potential majority elements efficiently.
Initialization:

count1, count2, candidate1, and candidate2 are initialized to 0 and 1. These variables are used to keep track of the counts and candidates for potential majority elements.
First Loop:

The first loop iterates through the elements in nums.
If the current number is equal to candidate1 or candidate2, the corresponding count is incremented.
If count1 or count2 is 0, the current number becomes a candidate, and the count is set to 1.
If both counts are non-zero, both counts are decremented.
Second Loop:

After the first loop, the function resets count1 and count2 to 0 and iterates through nums again to count occurrences of the potential majority candidates.
Result Calculation:

The function checks if the counts of the potential majority candidates (candidate1 and candidate2) are greater than ⌊ n/3 ⌋. If so, the candidates are added to the result list.
User Input:

The code then takes user input for the array. The user is prompted to enter elements separated by spaces.
Function Call and Print:

The majorityElement function is called with the user-input array, and the result is printed.
The code combines the Boyer-Moore Voting Algorithm with user input to find elements that appear more than ⌊ n/3 ⌋ times in the given array.
