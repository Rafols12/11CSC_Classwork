def get_colour():
    colour = input("Enter a colour: ")
    return colour

def print_colour_info(colour):
    print(colour.capitalize), len(colour)
def main():
    colour = []
    for i in range(5):
        colour = get_colour()
        colour.append(get_colour)
    print("nOutput:")
    for c in colour:
        print_colour_info(c)