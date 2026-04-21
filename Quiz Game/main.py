import os

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{50}"

import pgzrun

WIDTH = 870
HEIGHT = 650

#creating the rectangles
marquee_box = Rect(0,0,800,80)
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

def draw():
    screen.fill("white")

    #drawing the rectangles on the screen
    screen.draw.filled_rect(marquee_box,color="red")
    screen.draw.filled_rect(question_box,color="yellow")
    screen.draw.filled_rect(timer_box,color="purple")
    screen.draw.filled_rect(answer_box1,color="green")
    screen.draw.filled_rect(answer_box2,color="green")
    screen.draw.filled_rect(answer_box3,color="green")
    screen.draw.filled_rect(answer_box4,color="green")
    screen.draw.filled_rect(skip_box,color="blue")

pgzrun.go()