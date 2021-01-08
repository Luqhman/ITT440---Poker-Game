

player1_money = 1000
player2_money = 1000
dealer_cards = []
player1_cards = []
player2_cards = []
bet = 100
pc = 1
check = 0
hit = 0
playerID = 1
playerID1 = 1


#Player raise function
def betRaise(bet,player_money):
	player_bet = input("Enter amount to raise : (must be more than {bet}) ")
	player_money -= int(player_bet)
	bet = bet + int(player_bet)
	print("Player bet : " + player_bet)
	return bet, player_money

#asking a player to raise or hold
if playerID == playerID1:
	bet, player1_money = betRaise(bet,player1_money)
else:
	print("Not your turn!")



playerInput = input("Enter 1 to hit and 0 to check : ")
print(playerInput)

#if raise pc = 0, if hold pc = 1
if int(playerInput) == 1:
	hit = 1
	#send data to server
elif int(playerInput) == 0:
	check += 1
	#send data to server


#display for debugging purpose
print("Player money : " + str(player1_money))
print("Bet now : " + str(bet))

