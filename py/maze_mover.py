import location
import maze_printer
'''
maze_mover.pz contains recursive methods to transverse maze
'''
count = 0

def go_north(matrix):
    #sub 1 from current_row
    #if matrix[location.x][location.y] == ' ':
    matrix[location.x][location.y] = 'N'
    if (matrix[location.x][location.y - 1] == ' ' or matrix[location.x][location.y + 1] == ' ') and matrix[location.x - 1][location.y] != '#':
        location.set_stored_location()
        location.x -= 1
        return matrix
    if location.x - 1 > location.max_x:
        return matrix
    elif matrix[location.x - 1][location.y] == '#':
        return matrix
    elif matrix[location.x - 1][location.y] == 'E' or matrix[location.x - 1][location.y] == 'S' or matrix[location.x - 1][location.y] == 'W':
        return matrix
    else:
        location.x -= 1
        global count
        count += 1
        return go_north(matrix)

def go_east(matrix):
    #add 1 to current_column
    #if matrix[location.x][location.y] == ' ':
    matrix[location.x][location.y] = 'E'
    if (matrix[location.x + 1][location.y] == ' ' or matrix[location.x - 1][location.y] == ' ') and matrix[location.x][location.y + 1] != '#':
        location.set_stored_location()
        #location.y += 1
        return matrix
    #print("move # %i going east" %(count))
    if location.y + 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y + 1] == '#':
        return matrix
    elif matrix[location.x ][location.y + 1] == 'S' or matrix[location.x][location.y + 1] == 'W' or matrix[location.x][location.y + 1] == 'N':
        return matrix
    else:
        location.y += 1
        global count
        count += 1
        return go_east(matrix)

    return

def go_south(matrix):
    #add 1 to current_row
    #if matrix[location.x][location.y] == ' ':
    matrix[location.x][location.y] = 'S'
    if location.x + 1 > location.max_x:
        return matrix
    if (matrix[location.x][location.y + 1] == ' ' or matrix[location.x][location.y - 1] == ' ') and matrix[location.x + 1][location.y] != '#':
        location.set_stored_location()
        #location.x += 1
        return matrix
    elif matrix[location.x + 1][location.y] == '#':
        return matrix
    elif matrix[location.x + 1][location.y] == 'W' or matrix[location.x + 1][location.y] == 'N' or matrix[location.x + 1][location.y] == 'E':
        return matrix
    else:
        location.x += 1
        global count
        count += 1
        return go_south(matrix)

def go_west(matrix):
    #sub 1 to current_column
    #if matrix[location.x][location.y] == ' ':

    matrix[location.x][location.y] = 'W'
    #if matrix[location.x + 1][location.y] == ' ':
    if (matrix[location.x + 1][location.y] == ' ' or matrix[location.x - 1][location.y] == ' ') and matrix[location.x][location.y - 1] != '#':
        location.set_stored_location()
        #location.y -= 1
        return matrix
    if location.y - 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y - 1] == '#':
        return matrix
    elif matrix[location.x][location.y - 1] == 'E' or matrix[location.x][location.y - 1] == 'S' or matrix[location.x][location.y - 1] == 'W':
        return matrix
    else:
        location.y -= 1
        global count
        count += 1
        return go_west(matrix)

def start(matrix):
    global count
    location.init(0, 1, matrix)
    while location.x != 0 or location.y != 3:
        #recurse north
        print("move %i" % count)
        if location.x - 1 > 0 and matrix[location.x - 1][location.y] == ' ':
            matrix = go_north(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#' and matrix[location.x][location.y + 1] == '#':
                matrix[location.x][location.y] = 'X'
                location.get_stored_location()
        #recruse south
        elif location.x + 1 < location.max_x and matrix[location.x + 1][location.y] == ' ':
            matrix = go_south(matrix)
            if matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#' and matrix[location.x][location.y + 1] == '#':

                matrix[location.x][location.y] = 'X'
                location.get_stored_location()
        #recurse east
        elif matrix[location.x][location.y + 1] == ' ':
            matrix = go_east(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y + 1] == '#':
                matrix[location.x][location.y] = 'X'
                location.get_stored_location()
        #recruse west
        elif matrix[location.x][location.y - 1] == ' ':
            matrix = go_west(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#':
                matrix[location.x][location.y] = 'X'
                location.get_stored_location()

        maze_printer.print_matrix(matrix)
        print(location.log_properties())
        input()
        count += 1
        if location.x == 0 and location.y == 3:
            matrix[location.x][location.y] = '!'
    print("solution")
    return matrix
