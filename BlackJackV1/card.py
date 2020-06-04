#원래 코드

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit) #덱에 카드를추가하는 과정입니다.
    deck.remove('Q\u2663') # remove a queen as the game requires
    
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
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
    # Now, the deck should only have one card of each number


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print(' '.join(deck))
    
def get_valid_input():
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: num>=1
     '''
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


def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:"+str(tmp[1]))
     print("Do not worry. I cannot see the order of your cards")
     
     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(tmp[0])
     human=remove_pairs(tmp[1])

     print('Your current deck of cards is: ')
     
     print_deck(human)
     get_valid_input()


# main
if __name__=='__main__':
    play_game()