from tkinter import *
from PIL import Image, ImageTk
import random

mainWindow = Tk()
mainWindow.configure(background = "#808080")
mainWindow.title("Rock Paper Scissors")

rockSign = ImageTk.PhotoImage(Image.open("rock.png"))
rockSignComp = ImageTk.PhotoImage(Image.open("rockComp.png"))

paperSign = ImageTk.PhotoImage(Image.open("paper.png"))
paperSignComp = ImageTk.PhotoImage(Image.open("paperComp.png"))

scissorSign = ImageTk.PhotoImage(Image.open("scissor.png"))
scissorSignComp = ImageTk.PhotoImage(Image.open("scissorComp.png"))

#images/labels
player = Label(mainWindow, image = rockSign, bg = "#808080")
player.grid(row = 1, column = 0)
computer = Label(mainWindow, image = rockSignComp, bg = "#808080")
computer.grid(row = 1, column = 4)

#score of player
scorePlayer = Label(mainWindow, text = 0, font = 150, bg = "#808080", fg = "#FFFFFF")
scorePlayer.grid(row = 1, column = 1)

#scores of computer
scoreComputer = Label(mainWindow, text = 0, font = 150, bg = "#808080", fg = "#FFFFFF")
scoreComputer.grid(row = 1, column = 3)

#button for each option rock, paper, scissor
buttonRock = Button(mainWindow, width = 20, height = 2, text = "Rock", bg = "#FFFFFF", command = lambda:newPicture("buttonRock"))
buttonRock.grid(row = 2, column = 1)
buttonPaper = Button(mainWindow, width = 20, height = 2, text = "Paper", bg = "#FFFFFF", command = lambda:newPicture("buttonPaper"))
buttonPaper.grid(row = 2, column = 2)
buttonScissor = Button(mainWindow, width = 20, height = 2, text = "Scissor", bg = "#FFFFFF", command = lambda:newPicture("buttonScissor"))
buttonScissor.grid(row = 2, column = 3)

#button for exiting the function
exitButton = Button(mainWindow, width = 15, height = 2, text = "Click to Exit", command = mainWindow.destroy, bg = "#808080")
exitButton.grid(row = 3 , column = 2)



#indicator for each players side
userSide = Label(mainWindow, text = "PLAYER", font = 50, bg = "#808080")
userSide.grid(row = 0, column = 0)
compSide = Label(mainWindow, text = "COMPUTER", font = 50, bg = "#808080")
compSide.grid(row = 0, column = 4)

#messages for window
message = Label(mainWindow, font = 50, bg = "#808080", fg = "#FFFFFF")
message.grid(row = 1, column = 2)

def newMessage(msg):
    message["text"] = msg


#score update for player
def newScorePlayer():
    score = int(scorePlayer["text"])
    score += 1
    scorePlayer["text"] = str(score)

#score update for computer
def newScoreComp():
    score = int(scoreComputer["text"])
    score += 1
    scoreComputer["text"] = str(score)


#updating the pictures as button is clicked 
options = ["rock", "paper", "scissor"]

def newPicture(choice):

    choiceComp = options[random.randint(0,2)]
    winner(choice, choiceComp)
    if choiceComp == "rock":
        computer.configure(image = rockSignComp)
    elif choiceComp == "paper":
        computer.configure(image = paperSignComp)
    else: 
        computer.configure(image = scissorSignComp)

    if choice == "buttonRock":
        player.configure(image = rockSign)
    elif choice == "buttonPaper":
        player.configure(image = paperSign)
    else: 
        player.configure(image = scissorSign)


#changes text on main window and checks for winner by comparing different scenarios
def winner(player, computer):

    if player == "buttonRock" and computer == "rock":
        newMessage("Tie")
    elif player == "buttonPaper" and computer == "paper":
        newMessage("Tie")
    elif player == "buttonScissor" and computer == "scissor":
        newMessage("Tie")


    elif player == "buttonRock" and computer == "paper":
        newMessage("Computer Wins")
        newScoreComp()
    elif player == "buttonRock" and computer == "scissor":
        newMessage("Player Wins") 
        newScorePlayer()      


    elif player == "buttonPaper" and computer == "rock":
        newMessage("Player Wins")    
        newScorePlayer()
    elif player == "buttonPaper" and computer == "scissor":
        newMessage("Computer Wins")
        newScoreComp()


    elif player == "buttonScissor" and computer == "rock":
        newMessage("Computer Wins")
        newScoreComp()
    elif player == "buttonScissor" and computer == "paper":
        newMessage("Player Wins")
        newScorePlayer()


mainWindow.mainloop()