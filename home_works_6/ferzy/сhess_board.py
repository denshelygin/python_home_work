import random


def smite_queens(position):
    n = len(position)
    beat = False
    for i in range(n):
        for j in range(i + 1, n):
            if position[i][0] == position[j][0] or position[i][1] == position[j][1] or \
                    abs(position[i][0] - position[j][0]) == abs(position[i][1] - position[j][1]):
                beat = True
    if beat:
        return False
    else:
        return True


def good_position(need_count):
    position = []
    x_position = [1, 2, 3, 4, 5, 6, 7, 8]
    y_position = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 1
    count_iter = 0
    while count <= need_count:
        count_iter += 1
        random.shuffle(x_position)
        random.shuffle(y_position)
        for k in range(8):
            position.append([x_position[k], y_position[k]])

        if smite_queens(position):
            print(f'iteration = {count_iter}: {position}')
            count += 1
        position.clear()


if __name__ == '__main__':
    print(smite_queens([[1, 1], [2, 7], [3, 5], [4, 8], [5, 2], [6, 4], [7, 6], [8, 3]]))
    print(smite_queens([[1, 2], [2, 4], [3, 6], [4, 8], [5, 1], [6, 3], [7, 5], [8, 7]]))
    good_position(4)
