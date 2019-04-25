import location
import maze_printer
'''
maze_mover.pz contains recursive methods to transverse maze
'''
count = 0

def go_north(matrix):
    #sub 1 from current_row
    if matrix[location.x][location.y] == ' ':
        matrix[location.x][location.y] = 'N'
    #print("move # %i going north" %(count))
    if location.x - 1 > location.max_x:
        return matrix
    elif matrix[location.x - 1][location.y] == '#':
        return matrix
    elif matrix[location.x - 1][location.y] == 'E' or matrix[location.x - 1][location.y] == 'S' or matrix[location.x - 1][location.y] == 'W':
        return matrix
    elif matrix[location.x][location.y - 1] == ' ' or matrix[location.x][location.y + 1] == ' ':
        global stored_location
        location.set_stored_location()
        if matrix[location.x][location.y - 1] == ' ':
            location.direction = 'east'
        else:
            location.direction = 'west'
        return matrix
    else:
        location.x -= 1
        #maze_printer.print_matrix(matrix)
        global count
        count += 1
        return go_north(matrix)

def go_east(matrix):
    #add 1 to current_column
    if matrix[location.x][location.y] == ' ':
        matrix[location.x][location.y] = 'E'
    '''
    if matrix[location.x - 1][location.y] == ' ' or matrix[location.x + 1][location.y] == ' ':
        location.set_stored_location()

        if matrix[location.x - 1][location.y] == ' ':
            location.direction = 'north'
            location.x -= 1
        else:
            location.direction = 'south'
            location.x += 1

        return matrix
    '''
    #print("move # %i going east" %(count))
    if location.y + 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y + 1] == '#':
        return matrix
    elif matrix[location.x ][location.y + 1] == 'S' or matrix[location.x][location.y + 1] == 'W' or matrix[location.x][location.y + 1] == 'N':
        return matrix
    else:
        location.y += 1
        #maze_printer.print_matrix(matrix)
        global count
        count += 1
        return go_east(matrix)

    return

def go_south(matrix):
    #add 1 to current_row
    if matrix[location.x][location.y] == ' ':
        matrix[location.x][location.y] = 'S'
    global count
    #print("move # %i going south" %(count))
    if location.x + 1 > location.max_x:
        return matrix
    elif matrix[location.x + 1][location.y] == '#':
        return matrix
    elif matrix[location.x + 1][location.y] == 'W' or matrix[location.x + 1][location.y] == 'N' or matrix[location.x + 1][location.y] == 'E':
        return matrix
    elif matrix[location.x][location.y + 1] == ' ' or matrix[location.x][location.y - 1] == ' ':
        global stored_location
        location.set_stored_location()
        return matrix
    else:
        location.x += 1
        #maze_printer.print_matrix(matrix)
        count += 1
        return go_south(matrix)

def go_west(matrix):
    #sub 1 to current_column
    #if matrix[location.x][location.y] == ' ':
    if matrix[location.x + 1][location.y] == ' ' or matrix[location.x - 1][location.y] == ' ':
        matrix[location.x][location.y] = 'W'
    
    if matrix[location.x + 1][location.y] == ' ':
        location.direction = 'south'
    else:
        location.direction = 'north'
    print(location.direction)
    location.set_stored_location()
    return matrix

    #print("move # %i going west" %(count))
    if location.y - 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y - 1] == '#':
        return matrix
    elif matrix[location.x][location.y - 1] == 'E' or matrix[location.x][location.y - 1] == 'S' or matrix[location.x][location.y - 1] == 'W':
        return matrix
    else:
        location.y -= 1
        #maze_printer.print_matrix(matrix)
        global count
        count += 1
        return go_west(matrix)

def go_in_direction(matrix):
    if location.direction == "north":
        go_north(matrix)
    elif location.direction =="east":
        go_east(matrix)
    elif location.direction == "south":
        go_south(matrix)
    elif location.direction =="west":
        go_west(matrix)
    return matrix

def checkIfBranch(matrix):
    if location.direction != 'where':
        matrix = go_in_direction(matrix)
    location.direction = 'where'
    return matrix

def start(matrix):
    global count
    location.init(0, 1, matrix)
    while location.x != 0 or location.y != 3:
        #recurse north
        print("move %i" % count)
        if matrix[location.x - 1][location.y] == ' ':
            matrix = go_north(matrix)
        #recruse south
        elif matrix[location.x + 1][location.y] == ' ':
            matrix = go_south(matrix)
        #recurse east
        elif matrix[location.x][location.y + 1] == ' ':
            matrix = go_east(matrix)
        #recruse west
        elif matrix[location.x][location.y - 1] == ' ':
            matrix = go_west(matrix)
        maze_printer.print_matrix(matrix)
        matrix = checkIfBranch(matrix)
        if matrix[location.x - 1][location.y] == '#' and matrix[location.x][location.y + 1] == '#' and matrix[location.x][location.y + 1] == '#':
            matrix[location.x][location.y] = 'X'
            location.set_stored_location()
        count += 1
        #if matrix[location.x - 1][location.y] == '#'
        #print(location.direction)
    #print(location.log_properties())
    if location.x == 0 and location.y == 3:
        matrix[location.x][location.y] = '!'
    print("solution")
    return matrix
