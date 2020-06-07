#조커게임과 블랙잭 합쳐짐
#원카드 게임 추가 2020.6.5 .
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
import collections #collections 추가

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

#Creating 4 frames

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


#파일 경로 재지정

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
#메시지, 질문, 게임체인저
def Msgbox():
    tkinter.messagebox.showinfo("게임룰","딜러와 플레이어 중 카드의 합이 21 또는 21에 가장 가까운 숫자를 가지는 쪽이 이기는 게임입니다. \nAce는 1 또는 11로 계산합니다. \nKing, Queen, Jack은 각각 10으로 계산합니다.")
def Questionbox():
    tkinter.messagebox.askquestion("질문", "godh2138@gmail.com 로 이메일 주세요.")

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



def Gamechange(): 
    root.quit()
    root.destroy()
    Joker_start()

def Gamechange2(): 
    root.quit()
    root.destroy()
    onecard_start()


def onecard_start():
    onecardplay()


#게임변경 버튼
changebutton=Button(framedown2,text='joker play',  activebackground="green", font=button_font, padx=100,command=Gamechange)
changebutton.grid(row=0, column=2)
changebutton["fg"]="yellow"
changebutton["bg"]="pink"

change2button=Button(framedown2,text='onecard play',  activebackground="green", font=button_font, padx=100,command=Gamechange2)
change2button.grid(row=0, column=3)
change2button["fg"]="yellow"
change2button["bg"]="pink"

#규칙을 보여주는 팝업창 추가(블랙잭)
rule_button=Button(text="규칙을 보시겠습니까?",command=Msgbox)
rule_button.grid(row=1,column=1)
rule_button["fg"]="red"
rule_button["bg"]="white"

question_button=Button(root,text="질문 있으십니까?", width=15,command=Questionbox)
question_button.grid(row=1,column=2)
question_button["fg"]="red"
question_button["bg"]="white"

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
     message1="도둑잡기 (조커 픽) 카드 게임에  오신것을 환영합니다.\n플레이어의 현재 카드는: \n게임 실행하기 버튼을 누르세요\n"+str(tmp[1])
     "\n 게임진행하기버튼을 누르세요"
     
     w=Label(canvas,padx=10,justify=CENTER,font=button_font,text=message1).pack()
    
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


#게임변경 버튼
changebutton=Button(framedown2,text='joker play',  activebackground="green", font=button_font, padx=100,command=Gamechange)
changebutton.grid(row=0, column=2)
changebutton["fg"]="yellow"
changebutton["bg"]="pink"






#조커픽 함수 넣음

def wait_for_player():
    '''()->None
    사용자가 Enter 키를 누를 때까지 프로그램 일시 중지
    '''
    try:
         input("\n 엔터를 누르셔서 게임을 계속해주세요")
         print()
    except SyntaxError:
         pass


import random

def make_deck():
    '''()->list of str
        여왕이 없는채로 플레이할 덱을 나타내는 문자열을 반환
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Joker','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit) #덱에 카드를추가하는 과정입니다.
    deck.remove('Joker\u2663') # 게임에서 여왕을 제거한다.
    
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
      플레이할 덱을 나타내는 목록을 섞으시오    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    
     a={} #딕셔너리 사용필요
     dealer=[]
     human=[]
     for i in range(len(deck)):
         if i%2==0:
            dealer.append(deck[i]) #덱의 각 요소들이 추가된다.
         else:
            human.append(deck[i])
     return (dealer, human)

            
def remove_pairs(deck):
  
    a={} #딕셔너리 사용필요
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
    # 현재, 덱에는 각 번호의 카드가 한장씩 있어야한다.


def print_deck(deck):
    '''
    (list)-None
    공백을 구분하여 덱의 카드 요소들을 출력
    '''

    print(' '.join(deck))
    
def get_valid_input():
     '''
     (int)->int
     사용자가 지정한 정수를 최소 1부터 최대 n까지 반환
     사용자가 [1,n] 범위를 벗어나는 숫자를 지정하는한 범위안에 숫자를 지정할때까지 계속 요청
     
     Precondition: num>=1
     '''
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     while len(human)>1 or len(dealer)>1: #각 플레이어의 목록에 카드가 여러개 있는경우
         
         print('나는 '+str(len(dealer))+' 개의 카드를 가지고있다. 나는 1번부터 '+str(len(dealer))+' 번 카드를 가지고있는데, 내 카드중 어느것을 원하는가?')
         #num=0
         num=input('1 이랑 '+str(len(dealer))+' 사이의 숫자를 주십시오 : ')
         if int(num) < 1 or int(num)>len(dealer):
             num=input('잘못된 번호입니다. 1이랑 '+str(len(dealer)+'사이의 숫자를 입력해주세요'))
         if num==1:
             print ('너는 나의 '+str(int(num))+'첫번째','카드를 요청했다.')
         elif num==2:
             print ('너는 나의 '+str(int(num))+'두번째','카드를 요청했다.')
         elif num==3:
            print ('너는 나의 '+str(int(num))+'세번째','카드를 요청했다.')
         else:
             print ('너는 나의 '+str(int(num))+'네번째','카드를 요청했다.')
         print('여기 '+str(dealer[int(num)-1]+'이다.'))
         print('With '+str(dealer[int(num)-1]),' added,')
         print('당신의 현재 카드는: ')
         human.append(dealer[int(num)-1])
         dealer.remove(dealer[int(num)-1])
         print_deck(human)
         print('짝이 맞는 카드를 버린후 너의 카드는:')
         print_deck(remove_pairs(human))
         wait_for_player()

         print('My turn.')
         y=random.randint(1,len(remove_pairs(human)))
         if y==1:
             print ('나는 너의 '+str(int(y))+'첫번쨰','카드를 가져가겠다.')
         elif y==2:
             print ('나는 너의 '+str(int(y))+'두번쨰','카드를 가져가겠다.')
         elif y==3:
              print ('나는 너의 '+str(int(y))+'세번쨰','카드를 가져가겠다.')
         else:
              print ('나는 너의 '+str(int(y))+'네번쨰','카드를 가져가겠다.')

         dealer.append(human[y-1])
         human.remove(human[y-1])
         dealer=remove_pairs(dealer)
         human=remove_pairs(human)
         print('당신의 현재 카드는: ')
         print_deck(human)
         print('짝이 맞는 카드를 버린후 너의 카드는:')
         print_deck(remove_pairs(human))
         wait_for_player()

         if len(dealer)<1:
             break
         elif len(human)<1:
             break

     if len(remove_pairs(dealer))<1:
         print('나는 더이상의 카드가 없다.. \n 플레이어 패배')        

     if len(remove_pairs(human))<1:
         print('너는 더이상의 카드가 없다..\n 플레이어 승리')




         # 원카드


def getAvailable(hand, last_card, is_attack):
    available = []
    if not is_attack and last_card[0] == 'Joker':
        available.extend(hand)
        return available

    for card in hand:
        if card[0] == 'Joker':
            available.append(card)

        elif (card[0] != last_card[0]
              and card[1] != last_card[1]):
            continue

        elif is_attack:
            if get_damage(card) >= get_damage(last_card):
                available.append(card)
        else:
            available.append(card)

    return available


is_attack = False
damage = 1


def is_attack_card(card):
    return card[0] == 'Joker' or card[1] in ['A', '2']


damage_map = {
    'colored': 15,
    'black': 10,
    'A': 3,
    '2': 2
}


def get_damage(card):
    global damage_map
    return damage_map.get(card[1], 0)


def draw(hand):

    global put, deck

    hand.append(deck.pop())

    if len(deck) == 0:
        print("카드를 다시 섞습니다!")
        last_card = put.pop()
        random.shuffle(put)
        put, deck = deck, put
        put.append(last_card)


def card_str(card):
    return f'[{card[0]}{card[1]}]'


def hand_str(hand):
    return " ".join(map(card_str, hand))


message_count = 0
messages = []


def print_message(message):
    global put, deck, is_attack, messages, message_count, people
    player = people[0].hand
    os.system("cls")

    output = []
    output.append(f":: last put card ::  [[[{card_str(put[-1])}")
    output.append(f":: player's hand ::  {hand_str(player)}")
    output.append(
        f"::   available   ::  {hand_str(getAvailable(player, put[-1], is_attack))}")
    output.append("-" * 30)

    message_count += 1
    messages.append(message)
    if len(messages) == 16:
        messages.pop(0)
    for i, m in enumerate(messages):
        output.append(f'[{message_count - len(messages) + i + 1:>3}] {m}')
    output.append("-" * 30)

    print("\n".join(output))


def turn(person):
    # 전역 변수 접근
    global put, deck, is_attack, damage

    name = person.name
    hand = person.hand
    isComputer = person.is_computer

    # 차례
    print_message(f'{name}의 차례입니다.')

    # ----------- 낼 수 있는 카드 고르기 ---------------
    available = getAvailable(hand, put[-1], is_attack)

    # ----------- 카드 선택하기 ---------------------
    selected = None
    is_available = len(available) > 0
    if is_available:
        if isComputer:
            selected = random.choice(available)
        else:
            while True:
                i = input("몇 번째 카드를 내시겠습니까? "
                          "카드를 먹고 싶다면 0을 눌러주세요.")
                if not i.isdigit():
                    print_message("숫자를 입력해주세요.")
                    continue
                i = int(i) - 1
                if i >= len(available):
                    print_message("범위 내 숫자를 입력해주세요.")
                    continue
                if i != -1:
                    selected = available[i]
                break
    else:
        print_message(f'{name}가 낼 수 있는 카드가 없습니다.')

    # ------------선택한 카드 내기 -----------------------
    if selected is not None:
        hand.remove(selected)
        put.append(selected)

        if is_attack_card(selected):
            if not is_attack:
                damage = get_damage(selected)
            else:
                damage += get_damage(selected)

            is_attack = True

        print_message(f'{name}가 {selected}를 냈습니다."')

    # ------------ 카드 먹기 -----------------------
    else:
        print_message(f'{name}가 {damage}장 먹습니다.')
        if not isComputer:
            input("계속 하려면 엔터를 누르세요")
        is_attack = False
        for i in range(damage):
            draw(hand)
        damage = 1



#root.delete(ALL) -> tkinter 글씨들 지우기







def onecard():
   
    def getAvailable(hand, last_card, is_attack):
        available = []
        if not is_attack and last_card[0] == 'Joker':
            available.extend(hand)
            return available

        for card in hand:
            if card[0] == 'Joker':
                available.append(card)

            elif (card[0] != last_card[0]
                and card[1] != last_card[1]):
              continue

            elif is_attack:
                if get_damage(card) >= get_damage(last_card):
                    available.append(card)
            else:
                available.append(card)
    
        return available

    is_attack = False
    damage = 1

    def is_attack_card(card):
        return card[0] == 'Joker' or card[1] in ['A', '2']

    damage_map = {
        'colored': 15,
        'black': 10,
        'A': 3,
        '2': 2
        }
    
    def get_damage(card):
        global damage_mapreturn 
        return damage_map.get(card[1], 0)

    def draw(hand):
        global put, deck

        hand.append(deck,pop())

        if len(deck) == 0:
            print("카드를 다시 섞습니다!")
            last_card = put.pop()
            random.shuffle(put)
            put, deck = deck, put
            put.append(last.card)



    def card_str(card):
        return f'[{card[0]}{card[1]}]'

    def hand_str(hand):
        return "".join(map(card_str, hand))

    message_count = 0
    messages = []

    def print_message(message):
        global put, deck, is_attack, messages, message_count, people
        player = people[0].hand
        os.system("cls")

        output = []
        output.append(f":: last put card ::  [[[{card_str(put[-1])}")
        output.append(f":: player's hand :: {hand_str(player)}")
        output.append(
            f":: available :: {hand_str(getAvailable(player, put[-1], is_attack))}")
        output.append("-" * 30)


        message_count += 1
        messages.append(message)
        if len(massages) == 16:
            messages.pop(0)
        for i,m in enumerate(messages):
            output.append(f'[{message_count - len(messages) + i + 1:>3}] {m}')
        output.append("-" * 30)

        print("\n".join(output))


    def turn(person):
        #전역변수 접근
        global put, deck, is_attack, damage
        

        name = person.name
        hand = person.hand
        isComputer = person.is_computer

        #차례
        print_message(f'{name}의 차례입니다.')

        #낼수있는카드고르기
        available = getAvailable(hand, put[-1], is_attack)

        #카드선택하기
        selected = None
        is_available = len(available) > 0
        if is_available:
            if isComputer:
                selected = rendom.choice(available)
            else:
                while True:
                    i = input("몇 번째 카드를 내시겠습니까?"
                              "카드를 먹고 싶다면 0을 눌러주세요.")
                    if not i.isdigit():
                        print_message("숫자를 입력해주세요.")
                        continue
                    i = int(i) - 1
                    if i >= len(available):
                        print_message("범위 내 숫자를 입력해 주세요.")
                        continue
                    if i != -1:
                        selected = available[i]
                    break
        else:
            print_message(f'{name}가 낼수 있는 가드가 없습니다.')

        # 선택한 카드내기
        if selected is not None:
            hand.remove(selected)
            put.append(selected)

            if is_attack_card(selected):
                if not is_attack:
                    damage = get_damage(selected)
                else:
                    damage += get_damage(selected)
                is_attack = True
            print_message(f'{name}가 {selected}를 냈습니다"')

        #카드먹기
        else:
            print_message(f'{name}가 {damage}장 먹습니다.')
            if not isComputer:
                input("계속하려면 엔터를 누르세요")
            is_attack = False
            for i in range(damage):
                draw(hand)
            damage = 1

def onecardplay():
    global put, deck, is_attack, messages,  people
    deck = []

    shapes = '♥♣♠◆'
    nums = []
    for i in range(2,11):
        nums.append(str(i))
    for c in 'JQKA':
        nums.append(c)

    #덱만들기
    for shape in shapes:
        for num in nums:
            deck.append((shape, num))

    deck.append(('Joker', 'black'))
    deck.append(('Joker', 'colored'))
    random.shuffle(deck)


    #플레이어 정보를 받는 namedtuple생성
    Person = collections.namedtuple('Person', 'name hand is_computer')
    people = []

    # 플레이어 설정
    people.append(Person('플레이어', [], False))


    #컴퓨터 설정
    com_count = int(input('컴퓨터의 수를 입력해주세요 --> '))
    for i in range(com_count):
        people.append(Person(f'컴퓨터{i}', [], True))


    #플레이어에게 카드 나누기
    for i in range(7):
        for person in people:
            person.hand.append(deck.pop())


    #낸 카드에 하나 올려놓기
    put = []
    put.append(deck.pop())

    #게임 시작
    i= 0
    while True:
        current_person = people[i % len(people)]
        turn(current_person)
        if len(current_person.hand) == 0:
            print_message(f"{current_person.name}가 이겼습니다!")
            break
        i += 1









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
    global framecard
    resetpoint = 2
    framecard.destroy()
    framecard=Frame(root,width=150,height=150)
    framecard.grid(row=1, column = 0)
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
        
        text.insert(END,"\n딜러의 2번째 카드: "+str(card))
        while(computerTotal<21):
          
    
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