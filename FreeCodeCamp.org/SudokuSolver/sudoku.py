def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with 0
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (0)


def is_valid(puzzle, guess, row, col):
    # figure out whether the guess at the row/col of the puzzle is valid guess
    # return True if is valid, False otherwise

    # check the row
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # check the column
    # col_values = []
    # for r in range(9):
    #     col_values.append(puzzle[r][col])
    col_values = [puzzle[r][col] for r in range(9)]
    if guess in col_values:
        return False

    # check the 3x3 square
    # get where the 3x3 square starts and iterate over the 3 values in row/col
    row_start = (row // 3) * 3  # euclidean division : 1//3 = 0, 5//3 = 1
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if guess == puzzle[r][c]:
                return False

    # if we get here, these checks pass
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1 : if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  # range(1, 10) = 1, 2, 3, ..., 9

        # step 3: chef if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

            # step 5: if not valid OR if our guess does not solve the puzzle,
            # then we need to backtrack and try a new number
            puzzle[row][col] = 0  # reset the guess

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


def print_sudoku(puzzle):
    """Prints the sudoku board"""
    print("+" + "---+" * 9)
    for i, row in enumerate(puzzle):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+" * 9)
        else:
            print("+" + "   +" * 9)


if __name__ == '__main__':
    example_board = [
        [3, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 1, 9, 0, 8, 0],

        [0, 5, 0, 0, 6, 8, 0, 0, 0],
        [2, 0, 6, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],

        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 7, 0, 1, 0, 5, 0, 4, 0],
        [1, 0, 9, 0, 0, 0, 2, 0, 0]
    ]

    # almost impossible brute force sudoku
    example_board2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],

        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],

        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]

    print("The empty grid to solve:")
    print_sudoku(example_board)
    print("\nCalculating...", end=" ")
    is_solvable = solve_sudoku(example_board)
    print("Done.")
    print(f"\nThe sudoku is solvable? -> {is_solvable}")
    if is_solvable:
        input("Press ENTER to see the SOLVED sudoku...")
        print("\nHere, the solved sudoku:")
        print_sudoku(example_board)
    else:
        print("Sorry, it's impossible. Check your input. If it isn't your input,\
                there is a mistake in the sudoku you want to solve")
