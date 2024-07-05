import turtle
import pandas

#Load the data from 50_states
data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()

#Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Variables
correct_guesses = []
guessed_states = []

#Main game
while len(correct_guesses) <50:
    #User answer
    answer_state = screen.textinput(title = f'{len(correct_guesses)})/50 States Correct', prompt = "What's another State's name?").title()

    #Check if the guess is among the 50 states
    if answer_state in states_list:
        #Write correct guess on map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(answer_state)

        #Keep track of the correct guesses and update the score
        if answer_state in guessed_states:
            correct_guesses.append(answer_state)
            guessed_states.append(answer_state)

    #Update the title with current score
    screen.title(f'{len(correct_guesses)}/50 States Correct')
        
#Once all states are guessed, display the final score
trutle.write('Congratulations! You guessed all 50 states!', align = "center", font = ('Arial', 16, 'normal'))

#Keep the window open
screen.mainloop()




answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()

# your job is:
#1- using the 50_states.csv  file to check the user's answer against all of the states inside this file and see if it matches one of them
#2:when the user types in a state which is inside the 50_states.csv,then the state should be written onto the screen at the location where it exists.
#3:also keeping track of how many states users have guessed correctly out of 50,and every time they add a new state, then the number should be updates.