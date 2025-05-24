import random
total_game=0
dealer_score=0
player_score=0
def play_game():
    global total_game
    while total_game<3:

        print("Game:",total_game + 1)
        dealer_cards=[]
        player_cards=[]
        while len(dealer_cards)!=2:
            dealer_cards.append(random.randint(1,11))
        print("Dealer has x and:",dealer_cards[0])
        while len(player_cards)!=2:
            player_cards.append(random.randint(1,11))
        print("Player has",player_cards,"sum:",sum(player_cards))
        if sum(dealer_cards)==21:
            print("Sum of dealer cars is 21!You busted")
        elif sum(dealer_cards)>21:
            print("Sum of dealer cards is ",sum(dealer_cards),"\n and you won the game")
        while sum(dealer_cards)<21:
            action_take=input("You wanna stay or hit?")
            if action_take=="hit":
                player_cards.append(random.randint(1,11))
                print("cards are:",player_cards,"sum:",sum(player_cards))

            if sum(player_cards)>21:
                print("You lose")
            elif sum(player_cards)==21:
                print("You win")
                continue


            elif action_take=="stay":
                print("The sum of the dealer cards is",sum(dealer_cards))
                if sum(dealer_cards)>sum(player_cards):
                    print("Dealer win the game")
                elif sum(dealer_cards)<sum(player_cards):
                    print("You won the game")
                elif sum(dealer_cards)==sum(player_cards):
                    print("Match draw")
            break









        total_game+=1
play_game()

