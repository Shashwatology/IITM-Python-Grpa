
def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 
    
    Hint: final position = intial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    
    first = pos[0] + vel[0] * time
    second = pos[1] + vel[1] * time
    
    return (first,second)
