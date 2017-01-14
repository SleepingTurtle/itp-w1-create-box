"""This is the entry point of the program."""


def create_box(height, width, character):
    box =""
    for counter in range(height):
        box += (character * width)
        box += '\n'
    
    return box


if __name__ == '__main__':
    create_box(5, 24, 'x')
