def read_lines(text_path: str = ""):
    with open(text_path, 'r') as file:
        return file.readlines()
