US states Game project 

import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
guessed_states=[]
while len(guessed_states)<50:
  answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States correct" , prompt="What's another state name ?").title()
  print(answer_state)
  # def get_mouse_click_color(x,y):
  #   print(x,y)
  #
  # turtle.onscreenclick(get_mouse_click_color)
  #
  #turtle.mainloop()
  all_states=data.state.to_list() #or data["state"].to_list()

  if answer_state=="Exit":
    missing_states = []    # here we can use list comprehension , missing_states=[state for state in all_states if state not in guessed_states] 
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    #print(missing_states)
    new_data=pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break
  #if answer state is one of the states in all the states of the 50_states.csv
  if answer_state in all_states:
    guessed_states.append(answer_state)
    # create a turtle to write the name of the state to x and y coordinates
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    # t.write(state_data.state)  #contain additional information which is not required
    t.write(answer_state) or t.write(state_data.state.item())

#screen.exitonclick()
