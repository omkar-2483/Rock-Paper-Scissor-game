from tkinter import *
from PIL import Image,ImageTk #PIL=Python Imaging Library
from random import randint
import pygame

#start audio
pygame.mixer.init()    #initialization 
pygame.mixer.music.load('abhi_maza_aayega.mp3')
pygame.mixer.music.play(loops=0)

#def for other sounds
def play(a):
    if a=="lose":
        pygame.mixer.music.load('mood_kharab.mp3')
        pygame.mixer.music.play(loops=0)
    elif a=="win":
        pygame.mixer.music.load('jeet_gaye.mp3')
        pygame.mixer.music.play(loops=0)
    elif a=="tie":
        pygame.mixer.music.load('gadbad_hai.mp3')
        pygame.mixer.music.play(loops=0)
    elif a=="reset":
        pygame.mixer.music.load('shabbas_beta.mp3')
        pygame.mixer.music.play(loops=0)
    else:
        pass

#window
root = Tk()
root.title("ROCK PAPER SCISSOR GAME")
root.geometry("900x350")
filename=ImageTk.PhotoImage(Image.open("background.png"))
background=Label(root,image=filename)
background.place(x=0,y=0)
#root.state("zoomed")

#picture
player_rock = ImageTk.PhotoImage(Image.open("right rock.png"))
player_paper = ImageTk.PhotoImage(Image.open("right paper.png"))
player_scissor = ImageTk.PhotoImage(Image.open("right scissor.png"))
comp_rock = ImageTk.PhotoImage(Image.open("left rock.png"))
comp_paper = ImageTk.PhotoImage(Image.open("left paper.png"))
comp_scissor = ImageTk.PhotoImage(Image.open("left scissor.png"))

#insert picture
player_label = Label(root,image=player_scissor,bg="purple")
player_label.grid(row=1,column=4)
comp_label = Label(root,image=comp_scissor,bg="purple")
comp_label.grid(row=1,column=0)


#score
playerScore = Label(root, text=0, font=50, bg="black", fg="white")
compScore = Label(root, text=0, font=50, bg="black", fg="white")
compScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
player_indicator =  Label(root,font=50,text="PLAYER SCORE", bg="OrangeRed3", fg="white")
comp_indicator =  Label(root,font=50,text="COMPUTER SCORE", 
                        bg="OrangeRed3", fg="white")
player_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
msg = Label(root,font=50,bg="gray20",fg="cyan2")
msg.grid(row=3, column=2)

#update message
def updateMessage(a):
    msg['text'] = a

#update player score
def updatePlayerScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#update comp score

def updateCompScore():
    score = int(compScore["text"])
    score += 1
    compScore["text"] = str(score)

#function to reset
def reset():
    compScore["text"]=str(0)
    playerScore["text"]=str(0)
    play("reset")

#check winner
def checkWin(player,comp):
    if player == comp:
        updateMessage("IT's A TIE!")
        play("tie")
    elif player == "rock":
        if comp == "paper":
            updateMessage("YOU LOSE!")
            updateCompScore()
            play("lose")
        else:
            updateMessage("YOU WIN!")
            updatePlayerScore()
            play("win")
    elif player == "paper":
        if comp == "scissor":
            updateMessage("YOU LOSE!")
            updateCompScore()
            play("lose")
        else:
            updateMessage("YOU WIN!")
            updatePlayerScore()    
            play("win") 
    elif player == "scissor":
        if comp == "rock":
            updateMessage("YOU LOSE!")
            updateCompScore()
            play("lose")
        else:
            updateMessage("YOU WIN!")
            updatePlayerScore()  
            play("win")
    else:
            pass



#choice

choices = ["rock","paper","scissor"]


def updateChoice(a):

#comp
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=comp_rock)
    elif compChoice == "paper":
        comp_label.configure(image=comp_paper)
    else:
        comp_label.configure(image=comp_scissor)   


#player
    if a=="rock":
        player_label.configure(image=player_rock)
    elif a=="paper":
        player_label.configure(image=player_paper)
    else:
        player_label.configure(image=player_scissor)

    checkWin(a,compChoice)          





#buttons
rock = Button(root,width=20,height=2,text="ROCK",
              bg="gray4",fg="orange3",command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",
               bg="gray4",fg="red2",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",
                 bg="gray4",fg="DeepSkyBlue2",command = lambda:updateChoice("scissor")).grid(row=2,column=3)
Reset=Button(root,width=20,height=2,text="RESET"
                 ,bg="dark slate gray",fg="white",command=lambda:reset()).grid(row=4,column=1)
Exist=Button(root,width=20,height=2,text="EXIT",bg="dark slate gray",
                 fg="white",command=lambda:exit()).grid(row=4,column=3)

root.mainloop()