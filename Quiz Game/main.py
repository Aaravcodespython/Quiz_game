import os

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{50}"

import pgzrun

WIDTH = 870
HEIGHT = 650

score = 0
time_left = 10
game_over = False
question_count = 0
question_index = 0
file_name = "questions.txt"
questions = []

#creating the rectangles
marquee_box = Rect(0,0,870,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    global marquee_message
    screen.fill("white")

    #drawing the rectangles on the screen
    screen.draw.filled_rect(marquee_box, color="red")
    screen.draw.filled_rect(question_box, color="yellow")
    screen.draw.filled_rect(timer_box, color="purple")
    screen.draw.filled_rect(answer_box1, color="green")
    screen.draw.filled_rect(answer_box2, color="green")
    screen.draw.filled_rect(answer_box3, color="green")
    screen.draw.filled_rect(answer_box4, color="green")
    screen.draw.filled_rect(skip_box, color="blue")

    #adding texts on rectangles
    marquee_message = "Welcome to Quiz Game!"
    marquee_message = marquee_message + f" Q: {question_index} out of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color="white")
    screen.draw.textbox(str(time_left), timer_box, color="white", shadow=(0.5,0.5), scolor="black")
    screen.draw.textbox("Skip",skip_box, color="white", shadow=(0.5,0.5), scolor="black", angle=-45)

def move_marquee():
    marquee_box.x -= 2

    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    
    #open the file for reading
    qfile = open("questions.txt",mode="r")
    for line in qfile:
        questions.append(line)
        question_count += 1
    qfile.close()

def read_next_question():
    global question_index, questions

read_question_file()
print(questions)

pgzrun.go()
