from random import randint
import time
from tkinter import *
import tkinter.font
import os
import sys



#시작메뉴 추가
#배팅 시스템 추가
#리플레이시 초기화 문제 수정필요

global newDeck
root=Tk()
root.wm_title("블랙잭") #한글로 제목 수정

#게임내 폰트및 크기, 버튼 폰트및 크기 수정
game_font = tkinter.font.Font(family="맑은 고딕", size=10)
button_font = tkinter.font.Font(family="궁서체", size=10)

#Creating a window

#root.resizable(False, False) #게임 사이즈 변경 불가
root.minsize(300,150) #사이즈 수정필요


#Creating 2 frames

frameup=Frame(root,width=300,height=150)
frameup.pack()

framecard=Frame(root,width=150,height=150)
framecard.pack()


framedown =Frame(root,width=300,height=150)
framedown.pack()

#Creating text boxe in frameup

#배경색 변경
text=Text(frameup,bg='black',fg='white',font=game_font)
text.pack(fill=X)

imageA=tkinter.PhotoImage(file="C:\\A.png")
image2=tkinter.PhotoImage(file="C:\\2.png")
image3=tkinter.PhotoImage(file="C:\\3.png")
image4=tkinter.PhotoImage(file="C:\\4.png")
image5=tkinter.PhotoImage(file="C:\\5.png")
image6=tkinter.PhotoImage(file="C:\\6.png")
image7=tkinter.PhotoImage(file="C:\\7.png")
image8=tkinter.PhotoImage(file="C:\\8.png")
image9=tkinter.PhotoImage(file="C:\\9.png")
image10=tkinter.PhotoImage(file="C:\\10.png")
imageJ=tkinter.PhotoImage(file="C:\\J.png")
imageQ=tkinter.PhotoImage(file="C:\\Q.png")
imageK=tkinter.PhotoImage(file="C:\\K.png")






#버튼 폰트및 글자크기, 버튼크기 변경
hitbutton=Button(framedown,text="Hit",  activebackground="green", font=button_font, padx=100) 
hitbutton.pack(side=LEFT)


staybutton= Button(framedown,text="Stay",  activebackground="green", font=button_font, padx=100)
staybutton.pack(side=LEFT)

replaybutton=Button(framedown,text='Replay',  activebackground="green", font=button_font, padx=100)
replaybutton.pack(side=LEFT)


class deck(object):
	deck={"A":4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, "J":4, "Q":4, "K":4}
	cardsDict={1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K" }

	def __init__(self):
		text.insert(END,"\n카드들이 모두 섞였습니다.")

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
	if card=="A": #A를 10으로 11으로 할지 1로 할지 맨처음 게임 시작할떄 선택?
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
		
		text.insert(END,"\n당신의 카드: "+str(card))
		
		if playerTotal >21:
			
			text.insert(END,"\n당신은 패배했습니다! \n다시하려면 다시하기 버튼을 누르세요")
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
	
	playerAction=text.insert(END,"\n히트 아니면 스테이?")


def stay(event):
	global flag1
	global flag2
	global cardValue
	global computerTotal
	global card

	if flag1:
		
		text.insert(END,"\n딜러의 2번째 카드: "+str(card))
		while(computerTotal<21):
			card=newDeck.getCard()
			computerTotal+=cardValue(card)
			
			
			text.insert(END,"\n딜러의 카드: "+str(card))
			
			if computerTotal>playerTotal and computerTotal<21:
				
				text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기 버튼을 누르세요")
				break
			
			if computerTotal==21:
				if flag2:
					
					text.insert(END,"\n무승부!\n다시하려면 다시하기 버튼을 누르세요")
				else:
					
					text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기 버튼을 누르세요")

			elif computerTotal> 21:
				
				text.insert(END,"\n당신은 승리했습니다!\n다시하려면 다시하기 버튼을 누르세요")



def cardpic(card):

	if card == "A":
		label=tkinter.Label(framecard,image=imageA)
		label.pack()
		
	elif card == 2:
		label=tkinter.Label(framecard,image=image2)
		label.pack()

	elif card == 3:
		label=tkinter.Label(framecard,image=image3)
		label.pack()

	elif card == 4:
		label=tkinter.Label(framecard,image=image4)
		label.pack()

	elif card == 5:
		label=tkinter.Label(framecard,image=image5)
		label.pack()

	elif card == 6:
		label=tkinter.Label(framecard,image=image6)
		label.pack()

	elif card == 7:
		label=tkinter.Label(framecard,image=image7)
		label.pack()

	elif card == 8:
		label=tkinter.Label(framecard,image=image8)
		label.pack()

	elif card == 9:
		label=tkinter.Label(framecard,image=image9)
		label.pack()

	elif card == 10:
		label=tkinter.Label(framecard,image=image10)
		label.pack()

	elif card == "J":
		label=tkinter.Label(framecard,image=imageJ)
		label.pack()

	elif  card == "Q":
		label=tkinter.Label(framecard,image=imageQ)
		label.pack()

	elif  card == "K":
		label=tkinter.Label(framecard,image=imageK)
		label.pack()




def main():
	global newDeck
	global flag1
	global flag2
	global card
	global playerTotal
	global computerTotal
	text.delete('1.0',END)
	text.insert(END,"\n카드 섞는중...")

	
	newDeck=deck()
	flag1, flag2= True, False
	playerTotal, computerTotal=0,0

	
	card=newDeck.getCard()
	cardpic(card)
	

	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	cardpic(card)
	
	
	

	playerTotal=playerTotal+ cardValue(card)
	card=newDeck.getCard()
	

	text.insert(END,"\n딜러의 1번째 카드: "+ str(card))
	computerTotal+= cardValue(card)
	card=newDeck.getCard()
	computerTotal+= cardValue(card)

	action()

if __name__=='__main__':
	main()


image=tkinter.PhotoImage(file="C:\\Black.gif")
label=tkinter.Label(root,image=image)
label.pack()



staybutton.bind("<Button-1>",stay)
hitbutton.bind("<Button-1>",hit)
replaybutton.bind("<Button-1>",replay)
root.mainloop()






