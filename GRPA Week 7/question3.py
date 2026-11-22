import math
def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three points a, b, and c on the Cartesian plane, 
    calculate the Manhattan distance to go from point a to point c via point b.

    Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.

    Args:
        a (tuple): Coordinates of point a as (x1, y1).
        b (tuple): Coordinates of point b as (x2, y2).
        c (tuple): Coordinates of point c as (x3, y3).

    Returns:
        int: The Manhattan distance from point a to point c via point b.
    '''
    ...
    a1,a2 = a[0],a[1]
    b1,b2 = b[0],b[1]
    c1,c2 = c[0],c[1]
    
    distance_a_b = abs((b2-a2)) + abs((b1-a1)) 
    
    distance_b_c = abs((c2-b2)) + abs((c1-b1)) 
    
    return distance_b_c+distance_a_b
