import turtle
import random
import analyser
import math
import colour
import numpy as np

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LENGTH_FACTOR = 50
FORWARDS_STEP = 1


def initialisation():
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    turtle.colormode(255)


def de_init():
    turtle.done()


def draw_new_line(line: str):
    # create new turtle that will start at (0,0)
    t = turtle.Turtle()
    t.hideturtle()
    t.radians()

    # determine the sentiment score of each word and of the sentence itself
    score = get_line_score(line)
    score_words = []
    words_list = analyser.tokenize(line)
    for word in words_list:
        score_words.append(get_word_score(word))

    # determine the colors of each word (depends on neighbor words)
    colors = []
    for word in words_list:
        colors.append(get_word_color(word))

    draw_words(t, words_list, score_words, colors)


def get_line_score(line: str):
    return analyser.analyze(line)['compound']


def get_word_score(word: str):
    return analyser.analyze(word)['compound']


def get_word_color(word: str):
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_word(t: turtle.Turtle, word, new_score, color, old_color, width, old_width):
    # determine angle based on score
    t.left(math.acos(new_score))

    distance = len(word) * LENGTH_FACTOR
    move_forwards(t, distance, color, old_color, width, old_width)


def draw_words(t: turtle.Turtle, word_list, scores, colors):
    old_color = (255, 255, 255)
    old_width = 0
    for i in range(len(word_list)):
        word = word_list[i]
        print(word)
        new_score = scores[i]
        new_color = colors[i]
        width = max(int(math.sqrt(new_score ** 2) * 100), 10)
        draw_word(t, word, new_score, new_color, old_color, width, old_width)
        old_color = new_color
        old_width = width


def check_bounds(t: turtle.Turtle):
    screen = turtle.Screen()
    x, y = t.position()
    if x > screen.window_width() // 2:
        t.penup()
        t.setx(- screen.window_width() // 2)
        t.pendown()
    elif x < - screen.window_width() // 2:
        t.penup()
        t.setx( screen.window_width() // 2)
        t.pendown()
    if y > screen.window_height() // 2:
        t.penup()
        t.sety(-screen.window_height() // 2)
        t.pendown()
    elif y < -screen.window_height() // 2:
        t.penup()
        t.sety(screen.window_height() // 2)
        t.pendown()


def move_forwards(t: turtle.Turtle, distance: int, new_color, old_color, new_width, old_width):
    transition_colors_list = transition_color(old_color, new_color)
    transition_widths_list = transition_width(old_width, new_width)
    for i in range(distance//FORWARDS_STEP):
        if i < LENGTH_FACTOR//FORWARDS_STEP:
            t.pencolor(tuple(map(lambda x: int(x * 255), transition_colors_list[i].get_rgb())))
            t.width(transition_widths_list[i])
        t.forward(FORWARDS_STEP)
        check_bounds(t)


def transition_color(old_color, new_color):
    return list(colour.Color(rgb=tuple(map(lambda x: x / 255, old_color))).range_to(colour.Color(rgb=tuple(map(lambda x: x / 255, new_color))), LENGTH_FACTOR//FORWARDS_STEP))


def transition_width(old_width, new_width):
    return np.linspace(old_width, new_width, LENGTH_FACTOR//FORWARDS_STEP)
