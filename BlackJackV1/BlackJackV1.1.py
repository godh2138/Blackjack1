from random import randint
import time
from tkinter import *
from PIL import Image
import tkinter.font
import os
import sys



#시작메뉴 추가
#배팅 시스템 추가


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
frameup.grid(row=0, column = 0)

framecard=Frame(root,width=150,height=150)
framecard.grid(row=1, column = 0)


framedown =Frame(root,width=300,height=150)
framedown.grid(row=2, column = 0)

#Creating text boxe in frameup

#배경색 변경
text=Text(frameup,bg='black',fg='white',font=game_font)
text.grid(row=0, column = 0)

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
hitbutton.grid(row=0, column=0)


staybutton= Button(framedown,text="Stay",  activebackground="green", font=button_font, padx=100)
staybutton.grid(row=0, column=1)

replaybutton=Button(framedown,text='Replay',  activebackground="green", font=button_font, padx=100)
replaybutton.grid(row=0, column=2)


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


	#카드 사진저장
def cardpic(card):

	if card == "A":
		label=Label(framecard,image=imageA)
		label.grid(row=0, column = 0)
		
	elif card == 2:
		label=Label(framecard,image=image2)
		label.grid(row=0, column = 0)

	elif card == 3:
		label=Label(framecard,image=image3)
		label.grid(row=0, column = 0)

	elif card == 4:
		label=Label(framecard,image=image4)
		label.grid(row=0, column = 0)

	elif card == 5:
		label=Label(framecard,image=image5)
		label.grid(row=0, column = 0)

	elif card == 6:
		label=Label(framecard,image=image6)
		label.grid(row=0, column = 0)

	elif card == 7:
		label=Label(framecard,image=image7)
		label.grid(row=0, column = 0)

	elif card == 8:
		label=Label(framecard,image=image8)
		label.grid(row=0, column = 0)

	elif card == 9:
		label=Label(framecard,image=image9)
		label.grid(row=0, column = 0)

	elif card == 10:
		label=Label(framecard,image=image10)
		label.grid(row=0, column = 0)

	elif card == "J":
		label=Label(framecard,image=imageJ)
		label.grid(row=0, column = 0)

	elif  card == "Q":
		label=Label(framecard,image=imageQ)
		label.grid(row=0, column = 0)

	elif  card == "K":
		label=Label(framecard,image=imageK)
		label.grid(row=0, column = 0)




def cardpic1(card):

	if card == "A":
		label=Label(framecard, image=imageA)
		label.grid(row=0, column = 1)
		
	elif card == 2:
		label=Label(framecard,image=image2)
		label.grid(row=0, column = 1)

	elif card == 3:
		label=Label(framecard,image=image3)
		label.grid(row=0, column = 1)

	elif card == 4:
		label=Label(framecard,image=image4)
		label.grid(row=0, column = 1)

	elif card == 5:
		label=Label(framecard,image=image5)
		label.grid(row=0, column = 1)

	elif card == 6:
		label=Label(framecard,image=image6)
		label.grid(row=0, column = 1)

	elif card == 7:
		label=Label(framecard,image=image7)
		label.grid(row=0, column = 1)

	elif card == 8:
		label=Label(framecard,image=image8)
		label.grid(row=0, column = 1)

	elif card == 9:
		label=Label(framecard,image=image9)
		label.grid(row=0, column = 1)

	elif card == 10:
		label=Label(framecard,image=image10)
		label.grid(row=0, column = 1)

	elif card == "J":
		label=Label(framecard,image=imageJ)
		label.grid(row=0, column = 1)

	elif  card == "Q":
		label=Label(framecard,image=imageQ)
		label.grid(row=0, column = 1)

	elif  card == "K":
		label=Label(framecard,image=imageK)
		label.grid(row=0, column = 1)







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
			
			#이부분 총합을 보여주는것으로 변경요청
			text.insert(END,"\n딜러의 카드총합: "+str(card))
			
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
	cardpic1(card)
	
	
	

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
label.grid(row = 4, column = 0)



staybutton.bind("<Button-1>",stay)
hitbutton.bind("<Button-1>",hit)
replaybutton.bind("<Button-1>",replay)
root.mainloop()






