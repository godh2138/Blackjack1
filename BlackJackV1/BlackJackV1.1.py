#조커게임과 블랙잭 합쳐짐
from random import randint
import time
from tkinter import *
from PIL import Image
import tkinter.font
import os
import sys
from tkinter.constants import INSERT
import tkinter.messagebox
import sys
#from card import *

sys.setrecursionlimit(10000)
#시작메뉴 추가
money=2000
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

framedown2 =Frame(root,width=300,height=150)
framedown2.grid(row=3, column = 0)

#Creating text boxe in frameup

#배경색 변경
text=Text(frameup,bg='black',fg='white',font=game_font)
text.grid(row=0, column = 0)



imageA=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/BlackJackV1/9.png")
image2=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/2.png")
image3=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/3.png")
image4=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/4.png")
image5=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/5.png")
image6=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/6.png")
image7=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/7.png")
image8=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/8.png")
image9=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/9.png")
image10=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/10.png")
imageJ=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/j.png")
imageQ=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/q.png")
imageK=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/k.png")
#초기화 카드
imageR=tkinter.PhotoImage(file="C:/Users/user/git/Blackjack6/BlackJackV1/r.png")


#버튼 폰트및 글자크기, 버튼크기 변경
hitbutton=Button(framedown,text="Hit",  activebackground="green", font=button_font, padx=100) 
hitbutton.grid(row=0, column=0)
hitbutton["fg"]="red"
hitbutton["bg"]='pink'

staybutton= Button(framedown,text="Stay",  activebackground="green", font=button_font, padx=100)
staybutton.grid(row=0, column=1)
staybutton["fg"]="blue"
staybutton["bg"]="pink"
replaybutton=Button(framedown,text='Replay',  activebackground="green", font=button_font, padx=100)
replaybutton.grid(row=0, column=2)
replaybutton["fg"]="yellow"
replaybutton["bg"]="pink"

def next_game():
    
    canvas.destroy()
    canvas.quit()





def play_game():
     global canvas
     canvas=Tk() #조커픽 tk창
     canvas.wm_title("조커픽")
     canvas.minsize(500, 500)
     
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=remove_pairs(tmp[0])
     human=remove_pairs(tmp[1])
     dealer=tmp[0]
     human=tmp[1]
     message1="Hello. My name is Robot and I am the dealer.\nWelcome to my card game!\nYour current deck of cards is:\n"+str(tmp[1])
     "\nDo not worry. I cannot see the order of your cards\nNow discard all the pairs from your deck. I will do the same.\n게임시작버튼을 누르세요"
     
     w=Label(canvas,padx=10,justify=LEFT,font=button_font,text=message1).pack()
    
     b1=Button(canvas,text="게임을 실행하기",command=next_game)
     b1.pack(side=BOTTOM,padx=10)
     #w2=Label(canvas,padx=10,justify=LEFT,font=button_font,text=message1).pack()
     
     
     canvas.mainloop()
     get_valid_input()
     
def Joker_start():
    play_game()
    

def Msgbox():
    tkinter.messagebox.showinfo("게임룰","딜러와 플레이어 중 카드의 합이 21 또는 21에 가장 가까운 숫자를 가지는 쪽이 이기는 게임입니다. \nAce는 1 또는 11로 계산합니다. \nKing, Queen, Jack은 각각 10으로 계산합니다.")
def Questionbox():
    tkinter.messagebox.askquestion("질문", "godh2138@gmail.com 로 이메일 주세요.")
def Gamechange(): 
    root.quit()
    root.destroy()
    Joker_start()






changebutton=Button(framedown2,text='change',  activebackground="green", font=button_font, padx=100,command=Gamechange)
changebutton.grid(row=0, column=2)
changebutton["fg"]="yellow"
changebutton["bg"]="pink"
#규칙을 보여주는 팝업창 추가(블랙잭)
rule_button=Button(text="규칙을 보시겠습니까?",command=Msgbox)
rule_button.grid(row=1,column=1)
rule_button["fg"]="red"
rule_button["bg"]="white"

question_button=Button(root,text="질문 있으십니까?", width=15,command=Questionbox)
question_button.grid(row=1,column=2)
question_button["fg"]="red"
question_button["bg"]="white"



#조커픽 함수 넣음


def make_deck():
    
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit) #덱에 카드를추가하는 과정입니다.
    deck.remove('Q\u2663') # remove a queen as the game requires
    
    return deck

def shuffle_deck(deck):
    
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    
     a={} #need to use dictionary
     dealer=[]
     human=[]
     for i in range(len(deck)):
         if i%2==0:
            dealer.append(deck[i]) #append will add each element of the deck
         else:
            human.append(deck[i])
     return (dealer, human)

            
def remove_pairs(deck):
  
    a={} #need to use dictionary
    no_pairs = []
    for x in deck:
        if x[0] not in a:
            a[x[0]] = 1
        elif x[0] in a:
            a[x[0]] = a[x[0]] + 1
        else:
            a[x[0]] = a[x[0]] + 1
    for x in deck:
        if a[x[0]] % 2 == 0:
            a[x[0]] = 0
        else:
            no_pairs.append(x)
            a[x[0]] = 0
    random.shuffle(no_pairs)
    return no_pairs


###################################
'''def print_deck(deck):
    global canvas
    list4=' '.join(deck)
    print(list4)
    
    #text.insert(END,join(deck))'''
    
def get_valid_input():
     
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     while len(human)>1 or len(dealer)>1: #When there are multiple cards in each player's list
         
         print('I have '+str(len(dealer))+' cards. If 1 stands for my first card and '+str(len(dealer))+' for my last card, which of my cards would you like?')
         #num=0
         num=input('Give me an integer between 1 and '+str(len(dealer))+': ')
         if int(num) < 1 or int(num)>len(dealer):
             num=input('Invalid number. Please enter integer between 1 and '+str(len(dealer)))
         if num==1:
             print ('You asked for my '+str(int(num))+'st','card.')
         elif num==2:
             print('You asked for my '+str(int(num))+'nd','card.')
         elif num==3:
             print('You asked for my '+str(int(num))+'rd','card.')
         else:
             print('You asked for my '+str(int(num))+'th','card.')
         print('Here it is. It is '+str(dealer[int(num)-1]))
         print('With '+str(dealer[int(num)-1]),' added,')
         print('your current deck of cards are: ')
         human.append(dealer[int(num)-1])
         dealer.remove(dealer[int(num)-1])
         print_deck(human)
         print('And after discarding pairs and shuffling, your deck is:')
         print_deck(remove_pairs(human))
         wait_for_player()

         print('My turn.')
         y=random.randint(1,len(remove_pairs(human)))
         if y==1:
             print ('I took your '+str(int(y))+'st','card.')
         elif y==2:
             print('I took your '+str(int(y))+'nd','card.')
         elif y==3:
             print('I took your '+str(int(y))+'rd','card.')
         else:
             print('I took your '+str(int(y))+'th','card.')

         dealer.append(human[y-1])
         human.remove(human[y-1])
         dealer=remove_pairs(dealer)
         human=remove_pairs(human)
         print('your current deck of cards are: ')
         print_deck(human)
         print('And after discarding pairs and shuffling, your deck is:')
         print_deck(remove_pairs(human))
         wait_for_player()

         if len(dealer)<1:
             break
         elif len(human)<1:
             break

     if len(remove_pairs(dealer))<1:
         print('Ups. I do not have any more cards. \n You lost. I, robot, win.')        

     if len(remove_pairs(human))<1:
         print('Ups. You do not have any more cards.\n Congratulations. You, Human, win.')




# main

#play_game()



























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

    #카드 사진저장
def cardpic(card, count):
    

    if card == "A":
        label=Label(framecard,image=imageA)
        label.grid(row=0, column = count)
        ++count
        
    elif card == 2:
        label=Label(framecard,image=image2)
        label.grid(row=0, column = count)
        ++count

    elif card == 3:
        label=Label(framecard,image=image3)
        label.grid(row=0, column = count)
        ++count

    elif card == 4:
        label=Label(framecard,image=image4)
        label.grid(row=0, column = count)
        ++count

    elif card == 5:
        label=Label(framecard,image=image5)
        label.grid(row=0, column = count)
        ++count

    elif card == 6:
        label=Label(framecard,image=image6)
        label.grid(row=0, column = count)
        ++count

    elif card == 7:
        label=Label(framecard,image=image7)
        label.grid(row=0, column = count)
        ++count

    elif card == 8:
        label=Label(framecard,image=image8)
        label.grid(row=0, column = count)
        ++count

    elif card == 9:
        label=Label(framecard,image=image9)
        label.grid(row=0, column = count)
        ++count

    elif card == 10:
        label=Label(framecard,image=image10)
        label.grid(row=0, column = count)
        ++count

    elif card == "J":
        label=Label(framecard,image=imageJ)
        label.grid(row=0, column = count)
        ++count

    elif  card == "Q":
        label=Label(framecard,image=imageQ)
        label.grid(row=0, column = count)
        ++count

    elif  card == "K":
        label=Label(framecard,image=imageK)
        label.grid(row=0, column = count)
        ++count


def resetcard(count):
    global resetpoint
    label = Label(framecard, image = imageR)
    label.grid(row=0, column = resetpoint)



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
        global money
        global count
        global finish #게임종료후 hit 카드추가 안되게 수정
        card=newDeck.getCard()
        playerTotal=playerTotal+ cardValue(card)
        
        #카드그림 추가
        if finish == 0:
            count = count + 1
            cardpic(card,count)
        


        
        if playerTotal >21:
            money-=100
            text.insert(END,"\n당신은 패배했습니다! \n다시하려면 다시하기 버튼을 누르세요 남은 돈:")
            text.insert(END,money)
            flag1=False
            finish = 1

        elif playerTotal==21:
            finish = 1
            #give control to the computer, if he busts you win
        
            
            flag2=True
        else:
            action()
        




def replay(event):
    global count
    global resetpoint
    resetpoint = 2
    while(resetpoint <= count):
        resetcard(card)
        resetpoint = resetpoint + 1
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
    global finish

    if flag1:
        
        text2.insert(END,"\n딜러의 2번째 카드: "+str(card))
        while(computerTotal<21):
            card=newDeck.getCard()
            computerTotal+=cardValue(card)
    
            #딜러의 카드 총합으로 수정
            text.insert(END,"\n딜러의 카드총합: "+str(computerTotal))
            
            if computerTotal>playerTotal and computerTotal<21:
                
                text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기 버튼을 누르세요")
                break
            
            if computerTotal==21:
                if flag2:
                    
                    text.insert(END,"\n무승부!\n다시하려면 다시하기 버튼을 누르세요")
                    finish = 1
                else:
                    finish = 1
                    text.insert(END,"\n당신은 패배했습니다!\n다시하려면 다시하기 버튼을 누르세요")

            elif computerTotal> 21:
                finish = 1
                text.insert(END,"\n당신은 승리했습니다!\n다시하려면 다시하기 버튼을 누르세요")



def main():
    global newDeck
    global flag1
    global flag2
    global card
    global playerTotal
    global computerTotal
    global finish
    global count

    
    text.delete('1.0',END)
    text.insert(END,"\n카드 섞는중...")
    count = 0
    finish = 0

    
    newDeck=deck()
    flag1, flag2= True, False
    playerTotal, computerTotal=0,0

    
    card=newDeck.getCard()
    cardpic(card,count)
    count = count + 1

    
    

    playerTotal=playerTotal+ cardValue(card)
    card=newDeck.getCard()
    cardpic(card,count)
    

    
    
    

    playerTotal=playerTotal+ cardValue(card)
    card=newDeck.getCard()
    

    text.insert(END,"\n딜러의 1번째 카드: "+ str(card))
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

#root.delete(ALL) -> tkinter 글씨들 지우기
