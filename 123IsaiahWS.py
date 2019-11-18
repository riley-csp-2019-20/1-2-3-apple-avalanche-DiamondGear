import turtle as trtl
import random as rand

apple_image = "apple.gif"
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

screen_width = 400
screen_height = 400

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("tree.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

def reset_apple(active_apple):
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    create_apple(active_apple, letter_list.pop(index))

# given a turtle, set that turtle to be shaped by the image file
def create_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  wn.update()


def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)



def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 64,"bold"))
  active_apple.setpos(remember_position)
  apple.showturtle()


create_apple(apple, "A")

wn.onkeypress(drop_apple, "a")
wn.onkeypress(drop_apple, "b")
wn.onkeypress(drop_apple, "c")
wn.onkeypress(drop_apple, "d")
wn.onkeypress(drop_apple, "e")
wn.onkeypress(drop_apple, "f")
wn.onkeypress(drop_apple, "g")
wn.onkeypress(drop_apple, "h")

wn.listen()
trtl.mainloop()
