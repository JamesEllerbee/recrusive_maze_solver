#Author: James Ellerbee
#Project Purpose: Exercise Recursion and code design
'''maze_printer.py defines a function for printing a maze for use in maze_mover.py and solver.py'''
def print_matrix(container):
    for row in container:
        for column in row:
            print(column, end = " ")
        print()