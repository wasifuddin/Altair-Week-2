def process_instructions(instructions, grid_size):
    grid_x, grid_y = grid_size
    # Setting Initial Coordinates
    x, y = 0, 0
    # Direction List
    direction = ['N', 'E', 'S', 'W']
    # Initial front facing direction
    front_facing = 'N'
    index = 0
    for cmd in instructions:
        # Handling the Direction Change
        if cmd == 'L':
            index = (index - 1) % 4
        elif cmd == 'R':
            index = (index + 1) % 4
        front_facing = direction[index]
        # Calculating the position change
        if cmd == 'F':
            # North Direction
            if front_facing == 'N' and y + 1 <= grid_y:
                y += 1
            # South Direction
            elif front_facing == 'S' and y - 1 > -1:
                y -= 1
            # West Direction
            elif front_facing == 'W' and x - 1 > -1:
                x -= 1
            # East Direction
            elif front_facing == 'E' and grid_x + 1 <= grid_x:
                x += 1

    # Returning the Position Coordinates and the Front Facing Direction
    return (x, y,), front_facing


instructions = "FFLFFRFL"
grid_size = (5, 5)
print(process_instructions(instructions, grid_size))
