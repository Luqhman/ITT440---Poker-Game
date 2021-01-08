import itertools
from random import choice
import re



#creating deck
cards=["Aclubs","Adiamonds","Ahearts","Aspades","2clubs","2diamonds","2hearts","2spades","3clubs","3diamonds",\
	"3hearts","3spades","4clubs","4diamonds","4hearts","4spades","5clubs","5diamonds","5hearts","5spades","6clubs",\
	"6diamonds","6hearts","6spades","7clubs","7diamonds","7hearts","7spades","8clubs","8diamonds","8hearts","8spdaes",\
	"9clubs","9diamonds","9hearts","9spades","10clubs","10diamonds","10hearts","10spades","Jclubs","Jdiamonds",\
	"Jhearts","Jspades","Qclubs","Qdiamonds","Qhearts","Qspades","Kclubs","Kdiamonds","Khearts","Kspades"]


dealer_cards = []
dealer_point = 0
player1_cards = []
player1_point = 0
player2_cards = []
player2_point = 0
player1_money = 1000
player2_money = 1000
pcount = 2
dcount = 2
bet = 100
check = 0
hit = 1

#assign player cards
def assignPlayer1Card(start,end):
	for i in range(start,end):
		random_cards = choice(cards)
		player1_cards.append(random_cards)
		cards.remove(random_cards)

def assignPlayer2Card(start,end):
	for i in range(start,end):
		random_cards = choice(cards)
		player2_cards.append(random_cards)
		cards.remove(random_cards)


#assign table cards
def assignDealerCard():
	for i in range(len(dealer_cards),dcount):
		random_cards = choice(cards)
		dealer_cards.append(random_cards)
		cards.remove(random_cards)

#call function assign
assignPlayer1Card(len(player1_cards),pcount)
assignPlayer2Card(len(player2_cards),pcount)
assignDealerCard()

#print player and dealer card for debuggin purpose(buang je kalau nak)
print(player1_cards)
print(player2_cards)
print(dealer_cards)
print(len(cards))


#after accept data from client
#check whether the input from player 1 or player 2
if hit == 1:
	pcount += 1
	#make a if statement to check player 1 or 2 is hitting
	assignPlayer1Card(len(player1_cards),pcount)

print(player1_cards)



#get point function
def getPoint(cardStrength,player_point):
	if re.search("^A",cardStrength):
		if player_point + 11 <= 21:
			point = 11
		else:
			point = 1
	elif re.search("^2",cardStrength):
		point = 2
	elif re.search("^3",cardStrength):
		point = 3
	elif re.search("^4",cardStrength):
		point = 4
	elif re.search("^5",cardStrength):
		point = 5
	elif re.search("^6",cardStrength):
		point = 6
	elif re.search("^7",cardStrength):
		point = 7
	elif re.search("^8",cardStrength):
		point = 8
	elif re.search("^9",cardStrength):
		point = 9
	elif re.search("^10",cardStrength):
		point = 10
	elif re.search("^J",cardStrength):
		point = 10
	elif re.search("^Q",cardStrength):
		point = 10
	elif re.search("^K",cardStrength):
		point = 10
	else:
		print("cannot calculate point")

	point = point + player_point
	return point

#calculate point player and dealer
for i in range(len(player1_cards)):
	player1_point = getPoint(player1_cards[i],player1_point)
for i in range(len(player2_cards)):
	player2_point = getPoint(player2_cards[i],player2_point)
for i in range(len(dealer_cards)):
	dealer_point = getPoint(dealer_cards[i],dealer_point)

#print point player and dealer(buang je kalau nak)
print("Player 1 point : " +str( player1_point))
print("Player 2 point : " + str(player2_point))
print("Dealer point : " + str(dealer_point))














