#Author: James Ellerbee
#Project Purpose: Exercise Recursion and code design
import location
import maze_printer
'''
maze_mover.pz contains recursive methods to transverse maze
'''
def go_north(matrix):
    matrix[location.x][location.y] = 'N'
    if (matrix[location.x][location.y - 1] == ' ' or matrix[location.x][location.y + 1] == ' ') and matrix[location.x - 1][location.y] != '#':
        location.push_current_location()
        location.x -= 1
        return matrix
    if location.x - 1 > location.max_x:
        return matrix
    elif matrix[location.x - 1][location.y] == '#':
        return matrix
    else:
        location.log_path('N')
        location.x -= 1
        location.count += 1
        return go_north(matrix)

def go_east(matrix):
    matrix[location.x][location.y] = 'E'
    if (matrix[location.x + 1][location.y] == ' ' or matrix[location.x - 1][location.y] == ' ') and matrix[location.x][location.y + 1] != '#':
        location.push_current_location()
        #if matrix[location.x - 1][location.y] == ' ':
            #print("hi")
            #location.x -= 1
        return matrix
    if location.y + 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y + 1] == '#':
        #branching updates location to go in a direction.
        if matrix[location.x - 1][location.y] == ' ':
            location.log_path('N')
            location.x -= 1
        else:
            location.log_path('S')
            location.x += 1
        return matrix
    else:
        location.log_path('E')
        location.y += 1
        location.count += 1
        return go_east(matrix)

    return

def go_south(matrix):
    matrix[location.x][location.y] = 'S'
    if location.x + 1 > location.max_x:
        return matrix
    if (matrix[location.x][location.y + 1] == ' ' or matrix[location.x][location.y - 1] == ' ') and matrix[location.x + 1][location.y] != '#':
        location.push_current_location()
        location.x += 1
        return matrix
    elif matrix[location.x + 1][location.y] == '#':
        return matrix
    else:
        location.log_path('S')
        location.x += 1
        location.count += 1
        return go_south(matrix)

def go_west(matrix):
    matrix[location.x][location.y] = 'W'
    if (matrix[location.x + 1][location.y] == ' ' or matrix[location.x - 1][location.y] == ' ') and matrix[location.x][location.y - 1] != '#':
        location.push_current_location()
        #location.y -= 1
        return matrix
    if location.y - 1 > location.max_y:
        return matrix
    elif matrix[location.x][location.y - 1] == '#':
        return matrix
    else:
        location.log_path('W')
        location.y -= 1
        location.count += 1
        return go_west(matrix)

def canFinish(matrix):
    results = []
    if location.x == 0 and location.y == 3:
        matrix[0][3] = '!'
        results.append('Solved!')
        results.append(matrix)
    elif (location.x == 1 and location.y == 3) and matrix[0][3] == '#':
        results.append('Unsolvable!')
        results.append(matrix)
    return results

def start(matrix):
    location.init(0, 1, matrix)
    solved = False
    result = ''
    while not solved:
        #recurse north
        print("move %i" % location.count)
        if location.x - 1 > 0 and matrix[location.x - 1][location.y] == ' ':
            matrix = go_north(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#' and matrix[location.x][location.y + 1] == '#':
                matrix[location.x][location.y] = 'X'
                if not (location.x == 1 and location.y == 3):
                    location.pop_stored_location()
        #recruse south
        elif location.x + 1 < location.max_x and matrix[location.x + 1][location.y] == ' ':
            matrix = go_south(matrix)
            if matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#' and matrix[location.x][location.y + 1] == '#':

                matrix[location.x][location.y] = 'X'
                location.pop_stored_location()
        #recurse east
        elif matrix[location.x][location.y + 1] == ' ':
            matrix = go_east(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y + 1] == '#':
                matrix[location.x][location.y] = 'X'
                location.pop_stored_location()
        #recruse west
        elif matrix[location.x][location.y - 1] == ' ':
            matrix = go_west(matrix)
            if matrix[location.x - 1][location.y] == '#' and matrix[location.x + 1][location.y] == '#' and matrix[location.x][location.y - 1] == '#':
                matrix[location.x][location.y] = 'X'
                location.pop_stored_location()
        maze_printer.print_matrix(matrix)
        #print(location.to_string_properties())
        print("\n\n\n\n")
        input("Press Enter to continue...")
        location.count += 1
        results = canFinish(matrix)
        if len(results) > 0:
            result = results[0]
            solved = True
            matrix = results[1]
    if result == "Unsolvable!":
        print(result)
    else:
        print(result + location.get_path())
    return matrix