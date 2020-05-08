# To hit type "Hit" 
# To stay type anything
#hit 과 stay 를 명확히 구분해야 할 것 같아요. 의견 부탁

from random import randint
import time

class deck(object):
	deck={"A":4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, "J":4, "Q":4, "K":4}
	cardsDict={1:"A", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K" }

	def __init__(self):
		print ("Deck was shuffled!")

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

def action():
	global playerTotal
	global newDeck
	global flag1
	global flag2
	time.sleep(2)
	playerAction=input("Do you hit or stay?")
	if playerAction=="Hit":
		card=newDeck.getCard()
		playerTotal=playerTotal+ cardValue(card)
		time.sleep(2)
		print("Your Card: "+str(card))
		
		if playerTotal >21:
			time.sleep(2)
			print ("You Lose!")
			flag1=False
		elif playerTotal==21:
			#give control to the computer, if he busts you win
			time.sleep(2)
			flag2=True
		else:
			time.sleep(2)
			action()
	
print("Shuffling Deck")
time.sleep(2)
newDeck=deck()
flag1, flag2= True, False
playerTotal, computerTotal=0,0

print("Player gets following cards")
card=newDeck.getCard()
time.sleep(2)

print ("First card: "+ str(card))
playerTotal=playerTotal+ cardValue(card)
card=newDeck.getCard()
time.sleep(2)

print ("Second Card: "+ str(card))
playerTotal=playerTotal+ cardValue(card)
card=newDeck.getCard()
time.sleep(2)

print ("Dealer's First Card: "+ str(card))
computerTotal+= cardValue(card)
card=newDeck.getCard()
computerTotal+= cardValue(card)

action()


if flag1:
	time.sleep(2)
	print("Dealer's Second Card: "+str(card))
	while(computerTotal<21):
		card=newDeck.getCard()
		computerTotal+=cardValue(card)
		time.sleep(2)
		
		print("Dealer's Card: "+str(card))
		
		if computerTotal>playerTotal and computerTotal<21:
			time.sleep(2)
			print ("You lose!")
			break
		
		if computerTotal==21:
			if flag2:
				time.sleep(2)
				print("Its a draw!")
			else:
				time.sleep(2)
				print("You Lose!")

		elif computerTotal> 21:
			time.sleep(2)
			print ("You Win!")

	




