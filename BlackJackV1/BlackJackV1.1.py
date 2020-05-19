from random import randint
import time
from tkinter import *
import tkinter.font
import os
import sys



#시작메뉴 추가
#의견 배팅 시스템 추가
#게임 여러 기능 추가(PUSH, INSURANCE)

global newDeck
root=Tk()
root.wm_title("블랙잭") #한글로 제목 수정
#Creating a window
root.minsize(900,1000) #사이즈 수정필요

#Creating 2 frames
frameup=Frame(root,width=800,height=960)
frameup.pack()

framedown =Frame(root,width=800,height=200)
framedown.pack()
#Creating text boxe in frameup

text=Text(frameup,width=60,height=30,bg='coral',fg='black')
text.pack(fill=X)


hitbutton=Button(framedown,text="Hit",  activebackground="green") #�궗�씠�쓽 怨듬갚�쓣 �뜑 二쇱옄
hitbutton.pack(side=LEFT)

staybutton= Button(framedown,text="Stay",  activebackground="green")
staybutton.pack(side=LEFT)

replaybutton=Button(framedown,text='Replay',  activebackground="green")
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
	if card=="A": #ACE�쓽 媛믪씠 10�씠 �맆吏� 1�씠�맆吏� �뙋�떒�빐二쇰뒗 �봽濡쒓렇�옩 ( �씠寃껋쓣 �슦由ш� 吏곸젒 議곗젙�븷 �닔 �엳�떎硫�?)
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
		
		text.insert(END,"\nYour Card: "+str(card))
		
		if playerTotal >21:
			
			text.insert(END,"\nYou Lose! \nPress Replay to play again")
			flag1=False
		elif playerTotal==21:
			#give control to the computer, if he busts you win
			
			flag2=True
		else:
			
			action()

def replay(event):
	main()


def action():
	global playerTotal
	global newDeck
	global flag1
	global flag2
	
	playerAction=text.insert(END,"\nDo you hit or stay?")


def stay(event):
	global flag1
	global flag2
	global cardValue
	global computerTotal
	global card

	if flag1:
		
		text.insert(END,"\nDealer's Second Card: "+str(card))
		while(computerTotal<21):
			card=newDeck.getCard()
			computerTotal+=cardValue(card)
			
			
			text.insert(END,"\nDealer's Card: "+str(card))
			
			if computerTotal>playerTotal and computerTotal<21:
				
				text.insert(END,"\nYou lose!\nPress Replay to play again")
				break
			
			if computerTotal==21:
				if flag2:
					
					text.insert(END,"\nIts a draw!\nPress Replay to play again")
				else:
					
					text.insert(END,"\nYou Lose!\nPress Replay to play again")

			elif computerTotal> 21:
				
				text.insert(END,"\nYou Win!\nPress Replay to play again")

def main():
	global newDeck
	global flag1
	global flag2
	global card
	global playerTotal
	global computerTotal
	text.delete('1.0',END)
	text.insert(END,"\nShuffling Deck...")
	
	newDeck=deck()
	flag1, flag2= True, False
	playerTotal, computerTotal=0,0

	
	text.insert(END,"\nPlayer gets following cards")
	card=newDeck.getCard()
	

	text.insert(END,"\nFirst card: "+ str(card))
	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	

	text.insert(END,"\nSecond Card: "+ str(card))
	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	

	text.insert(END,"\nDealer's First Card: "+ str(card))
	computerTotal+= cardValue(card)
	card=newDeck.getCard()
	computerTotal+= cardValue(card)

	action()


if __name__=='__main__':
	main()



staybutton.bind("<Button-1>",stay)
hitbutton.bind("<Button-1>",hit)
replaybutton.bind("<Button-1>",replay)
root.mainloop()



