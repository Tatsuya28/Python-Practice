""" ---------------------------------------canSum
Write a function `canSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.

The function should return a boolean indicating whether it is possible to generate the targetSum using numbers form the array or not.

You may ise an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.

7 , [2, 3] ==>      7
          -2    /       \    -3
                5       4
            /   \       |       \
            3   2       2       1
        /   |   | \     | \     |   \
        1   0   0 -1    0 -1    -1  -2


--------------------------------------------howSum
Write a function `howSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the targetSum. If there is no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.


--------------------------------------------bestSum
Write a function `howSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.

The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum

If there is a tie for the shortest combination, you may return any one of the shortest.

"""

import numpy


# m : targetSum
# n : numbers.length
# Brute Force
# O( n ^ m ) time complexity
# O( m ) space complexity
# With memoization
# O( n * m ) time complexity
# O( m ) space complexity
def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):  # if it is True
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


# m : targetSum
# n : numbers.length
# Brute Force
# O( n^m * m) time complexity
# O( m ) space complexity
# With memoization
# O( n * m * m) time complexity
# O( m * m ) space complexity
def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            memo[targetSum] = numpy.append(remainderResult, num, None)
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]


# m : targetSum
# n : numbers.length
# Brute Force
# O( n^m * m) time complexity
# O( m * m ) space complexity
# With memoization
# O( n * m * m) time complexity
# O( m * m ) space complexity
def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = numpy.append(remainderCombination, num, None)
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination


print(f"\n------------------------- Test function: canSum -------------------------")
print(f"|   Target Sum: {7}     |   Array: {[2, 3]}         |   Possible? {canSum(7, [2, 3])}")         # true
print(f"|   Target Sum: {7}     |   Array: {[5, 3, 4, 7]}   |   Possible? {canSum(7, [5, 3, 4, 7])}")   # true
print(f"|   Target Sum: {7}     |   Array: {[2, 4]}         |   Possible? {canSum(7, [2, 4])}")         # false
print(f"|   Target Sum: {8}     |   Array: {[2, 3, 5]}      |   Possible? {canSum(8, [2, 3, 5])}")      # true
print(f"|   Target Sum: {300}   |   Array: {[7, 14]}        |   Possible? {canSum(300, [7, 14])}")      # false

print(f"\n------------------------- Test function: howSum -------------------------")
print(f"|   Target Sum: {7}     |   Array: {[2, 3]}         |   How? {howSum(7, [2, 3])}")              # [3. 2. 2.]
print(f"|   Target Sum: {7}     |   Array: {[5, 3, 4, 7]}   |   How? {howSum(7, [5, 3, 4, 7])}")        # [4. 3.]
print(f"|   Target Sum: {7}     |   Array: {[2, 4]}         |   How? {howSum(7, [2, 4])}")              # None
print(f"|   Target Sum: {8}     |   Array: {[2, 3, 5]}      |   How? {howSum(8, [2, 3, 5])}")           # [2. 2. 2. 2.]
print(f"|   Target Sum: {300}   |   Array: {[7, 14]}        |   How? {howSum(300, [7, 14])}")           # false

print(f"\n------------------------- Test function: bestSum -------------------------")
print(f"|   Target Sum: {7}     |   Array: {[5, 3, 4, 7]}   |   Best? {bestSum(7, [5, 3, 4, 7])}")       # [7.]
print(f"|   Target Sum: {8}     |   Array: {[2, 3, 5]}      |   Best? {bestSum(8, [2, 3, 5])}")          # [3. 5.]
print(f"|   Target Sum: {8}     |   Array: {[1, 4, 5]}      |   Best? {bestSum(8, [1, 4, 5])}")          # [4. 4.]
print(f"|   Target Sum: {100}   |   Array: {[1, 2, 5, 25]}  |   Best? {bestSum(100, [1, 2, 5, 25])}")    # [25. 25. 25. 25.]
