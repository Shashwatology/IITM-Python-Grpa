'''
GrPA 3 - Composing functions - GRADED
Implement all the given functions that are used to solve the below problems.
Follow the path
You are given a matrix of size m x n consisting of ones (1) and zeros (0). There is a single continuous path formed with ones that starts from the rightmost cell in the last row (m-th row) with one and ends at leftmost cell in the first row with one in it. The path does not branch, and there is only one such path. Your task is to traverse along the path and print the coordinates of the path from start to end as tuples over multiple lines. The path can move vertically and horizontally.
Input
matrix = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]
'''

#answer 

def index_of_first_occurance(row:list,elem):
    '''Given a list find the index of first occurance of 1 in it'''
    return row.index(elem)


def index_of_last_occurance(row:list,elem):
    '''Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.'''
    reversed_row = row[::-1]
    index_in_reversed = reversed_row.index(elem)
    return len(row) - index_in_reversed - 1


def is_valid_coordinate(x:int,y:int, M):
    '''Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative'''
    return (0 <= x < len(M)) and (0 <= y < len(M[0])) 


def valid_adjacent_coordinates(x:int,y:int, M):
    '''Create a set of valid adjacent coordinates(indices) given x,y and a matrix M'''
    return {(x1, y1) for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid_coordinate(x1,y1, M)} # all the possible adjacent coordinates

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''Find the coordinate(indices) of the next coordinate that has the value in it. For the starting coordinate the prev_coords would be None'''
    curr_row, curr_column = curr_coords
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # direction for next position from current position -> left, right, up, down

    for direction in directions:
        next_row = curr_row + direction[0] # when direction[0] -> -1 for left and +1 for right
        next_column = curr_column + direction[1] # when direction[1] -> -1 for up and +1 for down

        if (0 <= next_row < len(M)) and (0 <= next_column < len(M[0])) and (M[next_row][next_column] == value) and ((next_row, next_column) != prev_coords):
            return (next_row, next_column)


def get_path_coordinates(M):
    '''Given the matrix m, find the path formed by 1 from the last row to the first row.'''
    x_start, x_end = len(M) - 1, 0
    y_start, y_end = index_of_last_occurance(M[-1], 1), index_of_first_occurance(M[0], 1)
    path = [(x_start, y_start)]
    curr_coords = (x_start, y_start)
    while curr_coords!= (x_end, y_end):
        next_coords = next_coordinate_with_value(curr_coords, 1, M, prev_coords=path[-2] if len(path) > 1 else None)
        if next_coords is None:
            break
        path.append(next_coords)
        curr_coords = next_coords
    return path


def print_path(M):
    path = get_path_coordinates(M)
    for coord in path:
        print(f"({coord[0]}, {coord[1]})")


def alternate_path(M):
    path = get_path_coordinates(M)
    for i, (x, y) in enumerate(path):
        M[x][y] = 1 if i % 2 == 0 else 2
    return M


def count_path(M):
    path = get_path_coordinates(M)
    count = len(path)
    for i, (x, y) in enumerate(reversed(path)):
        M[x][y] = count - i
    return M


def mirror_horizontally(M):
    path = get_path_coordinates(M)
    max_col = len(M[0]) - 1
    for i, j in path:
        M[i][max_col - j] = 1
    return M


def mirror_vertically(M):
    path = get_path_coordinates(M)
    max_row = len(M) - 1
    for i, j in path:
        M[max_row - i][j] = 1
    return M