# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    max_height = 0
    id_mountain = -1
    for mountain_index in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > max_height:
            max_height, id_mountain = mountain_h, mountain_index

    # The index of the mountain to fire on.
    print(id_mountain)
