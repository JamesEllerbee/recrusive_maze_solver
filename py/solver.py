#Author: James Ellerbee
#Project Purpose: Exercise Recursion and code design
'''solver.py contains logic for reading in maze file, setting up the maze matrix, and calling maze mover.py'''
import maze_mover
import maze_printer

def parse_list_size(f):
    mazeDimensions = f.readline()
    mazeDimensions = mazeDimensions.strip('\n')
    str_numList = mazeDimensions.split(' ')
    int_numList = []
    for element in str_numList:
        int_numList.append(int(element))
    matrix = [0] * int_numList[0]
    for index in range(len(matrix)):
        matrix[index] = [0] * int_numList[1]
    return matrix

def parse_lines(f, matrix):
    row = 0
    column = 0
    for line in f:
        line = line.strip('\n')
        #print(line)
        column = 0
        for character in line:
            matrix[row][column] = character
            column += 1
        row += 1
    return matrix

def main():
    fname = input("Please enter a maze file: ")
    f = open(fname, "r")
    matrix = parse_list_size(f)
    matrix = parse_lines(f, matrix)
    f.close()
    print("Using the maze in: " + fname)
    maze_printer.print_matrix(matrix)
    print()
    maze_printer.print_matrix(maze_mover.start(matrix))
main()