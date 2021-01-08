

player_money = 1000
bet = 100
pc = 1
player_cards = []
table_cards = []
raiseHold = 1

#Player raise function
def betRaise(bet,pc,player_money):
	player_bet = input("Enter amount to raise : (Enter 0 if want to call) ")
	player_money -= int(player_bet)
	bet = bet + int(player_bet)
	print("Player bet : " + player_bet)
	if pc >= 1:
		pc -= 1
	return bet, pc, player_money

#asking a player to raise or hold
print("Player money : " + str(player_money))
playerInput = input("Enter 1 to raise and 0 to hold : ")
print(playerInput)

#if raise pc = 0, if hold pc = 1
if int(playerInput) == 1:
	bet,pc,player_money = betRaise(bet,pc,player_money)
else:
	pc += 1
#data for player money, bet, and pc count
print("Player money : " + str(player_money))
print("Bet now : " + str(bet))
print("PC count : " + str(pc))

