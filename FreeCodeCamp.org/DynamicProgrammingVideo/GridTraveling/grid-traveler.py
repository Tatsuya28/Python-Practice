"""
We consider a grid m * n.
We want to determine how many paths we can make from the top left corner to the bottom right one by only moving either downwards or rightwards.

                    n
        +-------+-------+-------+
        |   E   |       |       |
        +-------+-------+-------+
     m  |       |       |       |   height
        +-------+-------+-------+
        |       |       |   S   |
        +-------+-------+-------+
                  width

    ==> Right, Right, Down, Down
        Right, Down, Right, Down
        Right, Down, Down, Right
        Down, Down, Right, Right
        Down, Right, Down, Right
        Down, Right, Right, Down

    ==> 6 paths possible !
"""


# O( 2 ^ [m+n] ) time complexity
# O( m + n ) space complexity
def gridTravelerNonOptimized(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return gridTravelerNonOptimized(m - 1, n) + gridTravelerNonOptimized(m, n - 1)


# Memoization
# O( m * n ) time complexity
# O( m + n ) space complexity
def gridTraveler(m, n, memo=None):
    if memo is None:
        memo = {}

    key = f"{m}, {n}"

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]


height = int(input("Please choose the height : "))
width = int(input("Please choose the width : "))

print(f"\nThere are {gridTraveler(height, width)} paths possible")

print(f"\n\n{gridTravelerNonOptimized(height, width)}")
