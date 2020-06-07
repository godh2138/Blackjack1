# To hit type "Hit"
# To stay type anything
#!/bin/sh
from random import randint
import time
from tkinter import *
import os
import sys
global newDeck

root=Tk()
root.wm_title("BlackJack")
#Creating a window
root.minsize(400,500)

#Creating 2 frames
frameup=Frame(root,width=300,height=480)
frameup.pack()

framedown =Frame(root,width=400,height=100)
framedown.pack()
#Creating text boxe in frameup

text=Text(frameup,width=60,height=30,bg='coral',fg='black')
text.pack(fill=X)


hitbutton=Button(framedown,text="Hit")
hitbutton.pack(side=LEFT)

staybutton= Button(framedown,text="Stay")
staybutton.pack(side=LEFT)

replaybutton=Button(framedown,text='Replay')
replaybutton.pack(side=LEFT)


class deck(object):
	deck={"A":4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, "J":4, "Q":4, "K":4}
	cardsDict={1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K" }

	def __init__(self):
		text.insert(END,"\nDeck was shuffled!")

	def getCard(self):
		global deck
		global cardsDict
		i=randint(1,13)
		if self.deck[self.cardsDict[i]] !=0:
			self.deck[self.cardsDict[i]]-=1
			return self.cardsDict[i]
		else:
			return self.getCard()



def cardValue(card):
	global playerTotal
	cardsDict={"A":1 , 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10 }
	if card=="A":
		if playerTotal<=10:
			return 11
		else:
			return 1
	else:
		return cardsDict[card]



def hit(event):
		global newDeck
		global playerTotal
		global flag1
		global flag2
		card=newDeck.getCard()
		playerTotal=playerTotal+ cardValue(card)
		time.sleep(2)
		text.insert(END,"\nYour Card: "+str(card))
		
		if playerTotal >21:
			time.sleep(2)
			text.insert(END,"\nYou Lose! \nPress Replay to play again")
			flag1=False
		elif playerTotal==21:
			#give control to the computer, if he busts you win
			time.sleep(2)
			flag2=True
		else:
			time.sleep(2)
			action()

def replay(event):
	main()


def action():
	global playerTotal
	global newDeck
	global flag1
	global flag2
	time.sleep(2)
	playerAction=text.insert(END,"\nDo you hit or stay?")


def stay(event):
	global flag1
	global flag2
	global cardValue
	global computerTotal
	global card

	if flag1:
		time.sleep(2)
		text.insert(END,"\nDealer's Second Card: "+str(card))
		while(computerTotal<21):
			card=newDeck.getCard()
			computerTotal+=cardValue(card)
			time.sleep(2)
			
			text.insert(END,"\nDealer's Card: "+str(card))
			
			if computerTotal>playerTotal and computerTotal<21:
				time.sleep(2)
				text.insert(END,"\nYou lose!\nPress Replay to play again")
				break
			
			if computerTotal==21:
				if flag2:
					time.sleep(2)
					text.insert(END,"\nIts a draw!\nPress Replay to play again")
				else:
					time.sleep(2)
					text.insert(END,"\nYou Lose!\nPress Replay to play again")

			elif computerTotal> 21:
				time.sleep(2)
				text.insert(END,"\nYou Win!\nPress Replay to play again")

def main():
	global newDeck
	global flag1
	global flag2
	global card
	global playerTotal
	global computerTotal
	text.insert(END,"Shuffling Deck...")
	time.sleep(2)
	newDeck=deck()
	flag1, flag2= True, False
	playerTotal, computerTotal=0,0


	text.insert(END,"\nPlayer gets following cards")
	card=newDeck.getCard()
	time.sleep(2)

	text.insert(END,"\nFirst card: "+ str(card))
	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	time.sleep(2)

	text.insert(END,"\nSecond Card: "+ str(card))
	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	time.sleep(2)

	text.insert(END,"\nDealer's First Card: "+ str(card))
	computerTotal+= cardValue(card)
	card=newDeck.getCard()
	computerTotal+= cardValue(card)

	action()

if __name__ == '__main__':
	main()

staybutton.bind("<Button-1>",stay)
hitbutton.bind("<Button-1>",hit)
replaybutton.bind("<Button-1>",replay)
root.mainloop()



