from random import randint
import time
from tkinter import *
import os
import sys


global newDeck
root=Tk()
root.wm_title("블랙잭") #�븳湲�濡� �젣紐� �닔�젙
#Creating a window
root.minsize(400,400) #�궗�씠利� �닔�젙�븘�슂
root.resizable(False, False) #寃뚯엫 �궗�씠利� 蹂�寃� 遺덇�

#Creating 2 frames
frameup=Frame(root,width=400,height=440)
frameup.pack()

framedown =Frame(root,width=400,height=100)
framedown.pack()
#Creating text boxe in frameup

text=Text(frameup,width=60,height=30,bg='coral',fg='black')
text.pack(fill=X)

canvas=Canvas(root,width=300,height=300)
canvas.pack()
img=PhotoImage(file="C:\\Black.png")
canvas.create_image(20,20,anchor=NW,image=img)
mainloop()
hitbutton=Button(framedown,text="히트",  activebackground="green") #寃뚯엫�쓽 諛곌꼍�깋�룄 �닔�젙.
hitbutton.pack(side=LEFT)

staybutton= Button(framedown,text="스테이",  activebackground="green")
staybutton.pack(side=LEFT)

replaybutton=Button(framedown,text='다시하기',  activebackground="green")
replaybutton.pack(side=LEFT)


class deck(object):
	deck={"A":4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, "J":4, "Q":4, "K":4}
	cardsDict={1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K" }

	def __init__(self):
		text.insert(END,"\n카드가 섞였습니다.")

	def getCard(self):
		global deck
		global cardsDict
		i=randint(1,13)
		if self.deck[self.cardsDict[i]] !=0:
			self.deck[self.cardsDict[i]]-=1
			return self.cardsDict[i]
		else:
			return self.getCard()



def user_cardValue(card):
	global playerTotal
	cardsDict={"A":1 , 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10 }
	if card=="A": #플레이어에게 A카드를 받으면 1 과 11 중에 선택하게끔 수정
		text.insert(END,"\n1과10중에고르세요.")
		choice=input("1 or 10")
		if choice==1:
			return 1
		elif choice==11:
			return 11
		#if playerTotal<=10:
			#return 11
		#else:
			#return 1
	
def computer_cardValue(card):
	global playerTotal
	cardsDict={"A":1 , 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10 }
	
	return cardsDict[card]	



def hit(event):
		global newDeck
		global playerTotal
		global flag1
		global flag2
		card=newDeck.getCard()
		playerTotal=playerTotal+ user_cardValue(card)
		
		text.insert(END,"\n플레이어의 카드: "+str(card))
		
		if playerTotal >21:
			
			text.insert(END,"\n당신은 패배했습니다! \n다시하려면 다시하기를 누르세요")
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
	
	playerAction=text.insert(END,"\nhit, stay 중 선택하세요")


def stay(event):
	global flag1
	global flag2
	global user_cardValue
	global computer_cardValue
	global computerTotal
	global card

	if flag1:
		
		text.insert(END,"\n딜러의 2번째 카드: "+str(card))
		while(computerTotal<21):
			card=newDeck.getCard()
			computerTotal+=computer_cardValue(card)
			
			
			text.insert(END,"\n딜러의 카드: "+str(card))
			
			if computerTotal>playerTotal and computerTotal<21:
				
				text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기를 누르세요")
				break
			
			if computerTotal==21:
				if flag2:
					
					text.insert(END,"\n비겼습니다 /n 다시하려면 다시하기를 누르세요")
				else:
					
					text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기를 누르세요")

			elif computerTotal> 21:
				
				text.insert(END,"\n당신은 승리했습니다!\n다시하려면 다시하기를 누르세요")

def main():
	global newDeck
	global flag1
	global flag2
	global card
	global playerTotal
	global computerTotal
	text.delete('1.0',END)
	text.insert(END,"\n카드를 섞는중...")
	
	newDeck=deck()
	flag1, flag2= True, False
	playerTotal, computerTotal=0,0

	
	text.insert(END,"\n플레이어가 받은 카드들..")
	card=newDeck.getCard()
	

	text.insert(END,"\n1플레이어의 1번째 카드: "+ str(card))
	playerTotal=playerTotal+ user_cardValue(card)
	card=newDeck.getCard()
	

	text.insert(END,"\n2플레이어의 2번째 카드: "+ str(card))
	playerTotal=playerTotal+ user_cardValue(card)
	card=newDeck.getCard()
	

	text.insert(END,"\n딜러의 1번째 카드: "+ str(card))
	computerTotal+= computer_cardValue(card)
	card=newDeck.getCard()
	computerTotal+= computer_cardValue(card)

	action()


if __name__=='__main__':
	main()



staybutton.bind("<Button-1>",stay)
hitbutton.bind("<Button-1>",hit)
replaybutton.bind("<Button-1>",replay)
root.mainloop()



