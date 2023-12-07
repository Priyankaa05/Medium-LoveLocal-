# Medium-LoveLocal-
Q 2.Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Explaination:
majorityElement Function:

The given code is an implementation of the Boyer-Moore Majority Vote algorithm to find elements that appear more than ⌊ n/3 ⌋ times in an array.

Initialization:

count1, count2, candidate1, and candidate2 are initialized to 0 and 1.
Majority Voting:

The first loop iterates through the array nums.
If the current number is equal to candidate1 or candidate2, the respective count is incremented.
If either count is 0, the current number becomes the new candidate, and its count is set to 1.
If both counts are non-zero, both counts are decremented.
Counting:

The second loop counts the occurrences of candidate1 and candidate2 in the array.
Result Generation:

If the count of candidate1 is greater than ⌊ n/3 ⌋, it is added to the result.
If the count of candidate2 is greater than ⌊ n/3 ⌋, it is added to the result.
Result Output:

The final result is printed.
Algorithm:
The algorithm uses the Boyer-Moore Majority Vote algorithm, which aims to find at most two candidates that may appear more than ⌊ n/3 ⌋ times in the array.

The algorithm performs two passes through the array, first for finding potential candidates and their counts, and second for counting the occurrences of these candidates.

The time complexity is O(n), where n is the length of the input array.

The space complexity is O(1) since the algorithm uses constant space for variables.

In summary, the code efficiently finds elements that appear more than ⌊ n/3 ⌋ times in an array using the Boyer-Moore Majority Vote algorithm.

