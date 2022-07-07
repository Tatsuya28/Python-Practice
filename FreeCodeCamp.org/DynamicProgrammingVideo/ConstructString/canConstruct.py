""" ---------------------------- canConstruct
Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return a boolean indicating whether the`target` can be constructed by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank`as many times as needed.

-------------------------------- canConstruct
Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return the number of ways that the`target` can be constructed by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank`as many times as needed.

-------------------------------- allConstruct
Write a function `allConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return a 2D array containing all the ways that the`target` can be constructed by concatenating elements of the `wordBank` array. Each element of the 2D array should represent one combination that constructs the `target`.

You may reuse elements of `wordBank`as many times as needed.
"""


# m : target.length
# n : wordBank.length
# Brute Force
# O( n ^ m  * m) time complexity
# O( m * m ) space complexity
# Memoized
# O( n * m * m) time complexity
# O( m * m ) space complexity
def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


# m : target.length
# n : wordBank.length
# Brute Force
# O( n ^ m  * m) time complexity
# O( m * m ) space complexity
# Memoized
# O( n * m * m) time complexity
# O( m * m ) space complexity
def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == '':
        return 1

    totalCount = 0

    for word in wordBank:
        if target.startswith(word):
            # numberWaysForRest = countConstruct(target.removeprefix(word), wordBank, memo)
            totalCount += countConstruct(target.removeprefix(word), wordBank, memo)
            # totalCount += numberWaysForRest

    memo[target] = totalCount
    return totalCount


# m : target.length
# n : wordBank.length
# Brute Force
# O( n ^ m  * m) time complexity
# O( m * m ) space complexity
# Memoized
# O( n * m * m) time complexity
# O( m * m ) space complexity
def allConstruct(target, wordBank):
    if target == '':
        return [[]]

    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            suffixWays = allConstruct(suffix, wordBank)
            [suffixWays[i].insert(0, word) for i in range(len(suffixWays))]
            result = result + [suffixWays[i] for i in range(len(suffixWays))]

    return result

# TODO corriger targetWays

# print(f"\n------------------------- Test function: canConstruct -------------------------")
# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                       # true
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))        # false
# print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))        # false
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e",
#     "ee",
#     "eee",
#     "eeee",
#     "eeeee",
#     "eeeeee",
#     "eeeeeee"]))        # false
#
#
# print(f"\n------------------------- Test function: countConstruct -------------------------")
# print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))                       # 2
# print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                       # 1
# print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))        # 0
# print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))        # 4
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e",
#     "ee",
#     "eee",
#     "eeee",
#     "eeeee",
#     "eeeeee",
#     "eeeeeee"]))        # 0
#
#
# print(f"\n------------------------- Test function: allConstruct -------------------------")
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))                   # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                   # [['abc', 'def']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))    # []
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e",
#     "ee",
#     "eee",
#     "eeee",
#     "eeeee",
#     "eeeeee",
#     "eeeeeee"]))
