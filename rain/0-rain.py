
#!/usr/bin/python3



def rain(walls):
    w = 0
    water = 0
    size = len(walls)
    prev_wall = 0

    if size <= 0:
        return w

    for a in range(size):

        if walls[a] >= walls[prev_wall]:
            prev_wall = a
            w = 0
        else:
            water += walls[prev_wall] - walls[a]
            w += walls[prev_wall] - walls[a]

    if prev_wall < size - 1:

    
        water -= w
    
        prev_pass_peak = prev_wall
        prev_wall = size - 1

        for a in range(size - 1, prev_pass_peak, -1):

            if walls[a] >= walls[prev_wall]:
                prev_wall = a
            else:
                water += walls[prev_wall] - walls[a]

    return water
