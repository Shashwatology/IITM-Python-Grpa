
def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max = []
    for row in matrix:
        count = 0
        for element in row:
            if element == 0: 
                count += 1
        max.append(count) 

    maximum_row = 0
    prev = 0
    for i in range(0,len(max)):
        if prev<max[i]:
            prev = max[i]
            maximum_row = i
            
    return maximum_row
