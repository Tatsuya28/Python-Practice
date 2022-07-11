w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# Borders of the search zone
upper_limit, left_limit = 0, 0
bottom_limit, right_limit = h - 1, w - 1

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir.__contains__('U'):  bottom_limit = y0 - 1
    if bomb_dir.__contains__('D'):  upper_limit = y0 + 1

    if bomb_dir.__contains__('R'):  left_limit = x0 + 1
    if bomb_dir.__contains__('L'):  right_limit = x0 - 1

    x0 = left_limit + (right_limit - left_limit) // 2
    y0 = upper_limit + (bottom_limit - upper_limit) // 2

    print(f"{x0} {y0}")
