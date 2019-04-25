#Author: James Ellerbee
#Project Purpose: Exercise Recursion and code design
'''location.py handles keeping up with the current location within the maze, where x = row, and y = column'''
x = 0
y = 0

max_x = 0
max_y = 0

stored_locations = []
path = []

count = 0

def init(init_x, init_y, matrix):
    '''initalizes location'''
    global x, y,max_x, max_y
    x = init_x
    y = init_y
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1

def to_string_properties():
    return "current x: " + str(x) + "\ncurrent y: " + str(y)
    ''' + "\ncurrent max x: " + str(max_x) + "\ncurrent max y: " + str(max_y)'''

def log_path(direction):
    global path
    path.append(direction)

def get_path():
    pathString = "Direct path from entrance to exit: "
    for ele in path:
        pathString += ele
    return pathString

def current_location():
    '''returns a list of x and y coordinates'''
    global x, y
    return [x, y]

def push_current_location():
    '''function handles putting the current x and y into the list of stored locations'''
    global x,y, stored_locations
    stored_locations.append([x,y])

def pop_stored_location():
    '''function handles setting the current x and y to the last element in the stored_locations list'''
    global x, y, stored_locations
    if(len(stored_locations) > 0):
        orderedPair = stored_locations.pop()
        x = orderedPair[0]
        y = orderedPair[1]


