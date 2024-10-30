import sentiment_analyser
import drawer
import reader
import pathlib


def main(text_path: str, save_image: bool = True):
    if not pathlib.Path(text_path).is_file():
        print(text_path + " is not a valid path. Please enter a valid path and try again")
        return
    sentiment_analyser.initialisation()
    drawer.initialisation()
    lines = reader.read_lines(text_path)
    for line in lines:
        drawer.draw_new_line(line)
    drawer.de_init()


if __name__ == '__main__':
    main('./examples/texts/colors.txt')
