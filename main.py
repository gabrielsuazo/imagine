import analyser
import drawer
import os
import reader


def main(text_path: str, save_image: bool = True):
    if not os.path.isfile(text_path):
        print(text_path + " is not a valid path. Please enter a valid path and try again")
        return
    analyser.initialisation()
    lines = reader.read_lines(text_path)
    for line in lines:
        drawer.draw_new_line(line)


if __name__ == '__main__':
    main('./examples/texts/the_raven.txt')
