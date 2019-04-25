'''location.py handles keeping up with the current location within the maze, where x = row, and y = column'''
x = 0
y = 0

max_x = 0
max_y = 0

stored_location = [0,0]
direction = 'where'

def init(init_x, init_y, matrix):
    '''initalizes location'''
    global x, y,max_x, max_y
    x = init_x
    y = init_y
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1

def log_properties():
    print("current x: " + str(x) + "\ncurrent y: " + str(y) + "\ncurrent max x: " + str(max_x) + "\ncurrent max y: " + str(max_y))

def north():
    '''decrements x'''
    global x
    return x - 1

def east():
    '''increments y'''
    global y
    return y + 1

def south():
    '''increments x'''
    global x
    return x + 1

def west():
    '''decrements y'''
    global y
    return y - 1

def current_location():
    '''returns a list of x and y coordinates'''
    global x, y
    return [x, y]

def set_stored_location():
    global stored_location
    stored_location = current_location()

def get_stored_location():
    global x, y, stored_location
    x = stored_location[0]
    y = stored_location[1]

def get_x():
    global x
    return x

def get_y():
    global y
    return y

