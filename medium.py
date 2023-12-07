{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59e801ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the elements of the array separated by space: [3,2,3]\n",
      "Elements that appear more than ⌊ n/3 ⌋ times: [3]\n"
     ]
    }
   ],
   "source": [
    "def majorityElement(nums):\n",
    "    if not nums:\n",
    "        return []\n",
    "\n",
    "    count1, count2, candidate1, candidate2 = 0, 0, 0, 1\n",
    "\n",
    "    for num in nums:\n",
    "        if num == candidate1:\n",
    "            count1 += 1\n",
    "        elif num == candidate2:\n",
    "            count2 += 1\n",
    "        elif count1 == 0:\n",
    "            candidate1, count1 = num, 1\n",
    "        elif count2 == 0:\n",
    "            candidate2, count2 = num, 1\n",
    "        else:\n",
    "            count1 -= 1\n",
    "            count2 -= 1\n",
    "\n",
    "    count1 = count2 = 0\n",
    "    for num in nums:\n",
    "        if num == candidate1:\n",
    "            count1 += 1\n",
    "        elif num == candidate2:\n",
    "            count2 += 1\n",
    "\n",
    "    result = []\n",
    "    if count1 > len(nums) // 3:\n",
    "        result.append(candidate1)\n",
    "    if count2 > len(nums) // 3:\n",
    "        result.append(candidate2)\n",
    "\n",
    "    return result\n",
    "\n",
    "\n",
    "user_input = input(\"Enter the elements of the array separated by space: \")\n",
    "nums = list(map(int, user_input.strip('[]').split(',')))\n",
    "\n",
    "result = majorityElement(nums)\n",
    "print(\"Elements that appear more than ⌊ n/3 ⌋ times:\", result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "700ef851",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
