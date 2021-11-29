from cs50 import get_int


def main():
    # Prompt for height
    while True:
        height = get_int("Height: ")
        if height < 1 or height > 8:
            height = get_int("Height: ")
        if 0 < height and height < 9:
            break
        return height
    
    # Build pyramid
    blocks = 1
    spaces = height - 1
    for i in range(height):
        printSpaces(spaces)
        printBlocks(blocks)
        print()
        spaces -= 1
        blocks += 1
 

# Print pyramid block        
def printBlocks(n):
    for i in range(n):
        print("#", end="")


# Print white space
def printSpaces(n):
    for i in range(n):
        print(" ", end="")


# Run programme    
if __name__ == "__main__":
    main()