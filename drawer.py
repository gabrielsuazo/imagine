import turtle
import random


def draw_new_line(line: str):
    # create new turtle that will start at (0,0)
    t = turtle.Turtle()
    t.hideturtle()
    turtle.colormode(255)

    # determine the sentiment score of each word and of the sentence itself
    score = get_line_score(line)
    score_words = []
    for word in line:
        score_words.append(get_word_score(word))

    # determine the colors of each word (depends on neighbor words)
    colors = []
    for word in line:
        colors.append(get_word_color(word))

    width = ""

    draw_words(t, line, score_words, colors)


def get_line_score(line: str):
    return random.uniform(0, 1)


def get_word_score(word: str):
    return random.uniform(0, 1)


def get_word_color(word: str):
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_word(t: turtle.Turtle, word, previous_score, new_score, color):
    t.pencolor(color)

    # determine angle based on score differential
    t.left(random.uniform(0, 360))

    distance = len(word) * 50
    t.forward(distance)


def draw_words(t: turtle.Turtle, line, scores, colors):
    previous_score = 0
    for i in range(len(line)):
        word = line[i]
        new_score = scores[i]
        new_color = colors[i]
        draw_word(t, word, previous_score, new_score, new_color)
        previous_score = new_score
