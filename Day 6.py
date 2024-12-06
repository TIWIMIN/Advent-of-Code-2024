file = open("input.txt", "r")

# Prepare the matrix
matrix = [list(line.strip()) for line in file]
width = len(matrix[0])
height = len(matrix)

# Initialize the boolean matrix
bool_matrix = [[False for _ in range(width)] for _ in range(height)]

# Movement directions
up, right, down, left = True, False, False, False
position = [0, 0]
sum = 0

# Locate the starting position
for m, row in enumerate(matrix):
    for n, item in enumerate(row):
        if item == "^":
            position = [m, n]
            matrix[m][n] = '.'  # Replace '^' with '.'
            bool_matrix[m][n] = True
            sum += 1  # Mark initial position as visited

# Traversal
while 0 <= position[0] < height and 0 <= position[1] < width:
    print("position:", position)
    if up:
        if position[0] - 1 < 0: 
            break
        if matrix[position[0] - 1][position[1]] == "#":
            up = False
            right = True
        else:
            print("up")
            position[0] -= 1

    elif right:
        if position[1] + 1 >= width: 
            break
        if matrix[position[0]][position[1] + 1] == "#":
            right = False
            down = True
        else:
            print("right")
            position[1] += 1

    elif down:
        if position[0] + 1 >= height: 
            break 
        if matrix[position[0] + 1][position[1]] == "#":
            down = False
            left = True
        else:
            print("down")
            position[0] += 1

    elif left:
        if position[1] - 1 < 0: 
            break 
        if matrix[position[0]][position[1] - 1] == "#":
            left = False
            up = True
        else:
            print("left")
            position[1] -= 1

    # Update the boolean matrix and sum
    if not bool_matrix[position[0]][position[1]]:
        bool_matrix[position[0]][position[1]] = True
        sum += 1

print(sum)
file.close()
