import os

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{50}"

import pgzrun

WIDTH = 870
HEIGHT = 650

score = 0
time_left = 10
is_game_over = False
question_count = 0
question_index = 0
file_name = "questions.txt"
question_set = []

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
    screen.draw.textbox(one_question_set[0].strip(), question_box, color="brown")
    
    index = 1

    for box in answer_boxes:
        screen.draw.textbox(one_question_set[index].strip(), box, color="navy")
        index += 1


def move_marquee():
    marquee_box.x -= 2

    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, question_set
    
    #open the file for reading
    qfile = open("questions.txt",mode="r")
    for line in qfile:
        question_set.append(line)
        question_count += 1
    qfile.close()

def read_next_question():
    global question_index, question_set

    #take the top question to be shown on the screen and remove it from the question_set list
    question_set_to_show = question_set.pop(0)
    question_index += 1
    
    #Each comma will break the sentence into a list using , as a criteria for the function
    return question_set_to_show.split(",")

def update_time_left():
    global time_left

    if time_left > 0:
        time_left -= 1
        
    else:
        game_over()

def game_over():
    global time_left, one_question_set, is_game_over

    is_game_over = True
    one_question_set = [f"Game Over, you scored {score} out of {question_count}","----------","----------","----------","----------",5]
    time_left = 0

def on_mouse_down(pos):
    index = 1
    #we are interested with the answers and not the question and the first answer is index number 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(one_question_set[5]):
                correct_answer()
            else:
                game_over()
        
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()
    
def correct_answer():
    global score, time_left, question_set, one_question_set
    
    score += 1

    if question_set:
        #this if condition is checking if there is items in the list
        one_question_set = read_next_question()
        time_left = 10

    else:
        game_over()


def skip_question():
    global time_left, one_question_set

    if question_set and is_game_over == False:
        one_question_set = read_next_question()
        time_left = 10

    else:
        game_over()



read_question_file()
one_question_set = read_next_question()
clock.schedule_interval(update_time_left,1)

pgzrun.go()
