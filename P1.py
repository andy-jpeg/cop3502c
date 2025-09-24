import p1_random as p1
rng = p1.P1Random()

player_wins = 0
dealer_wins = 0
game_count = 1

player_cards = 0
computer_cards = 0

card = 0
card_name = ""

validOption = True

def randomCard():
    return rng.next_int(13) + 1

def promptPlayer():
    print("1. Get another card\n"
          "2. Hold hand\n"
          "3. Print statistics\n"
          "4. Exit\n")

print(f"START GAME #{game_count}")

while True:
    if validOption:
        card = randomCard()
        if card == 1:
            card_name = "ACE"
        elif card > 1 and card < 11:
            card_name = str(card)
        else:
            if card == 11:
                card_name = "JACK"
            elif card == 12:
                card_name = "QUEEN"
            elif card == 13:
                card_name = "KING"

            card = 10

        if (player_cards + card) > 21:
            print(f"\nYour card is a {card_name}!")
            print(f"Your hand is: {player_cards + card}\n")

            print("You exceeded 21! You lose.\n")

            player_cards = 0
            computer_cards = 0

            dealer_wins += 1
            game_count += 1

            print(f"START GAME #{game_count}")
            continue
        elif (player_cards + card) == 21:
            print(f"\nYour card is a {card_name}!")
            print(f"Your hand is: {player_cards + card}\n")

            print("BLACKJACK! You win!\n")

            player_cards = 0
            computer_cards = 0

            game_count += 1
            player_wins += 1

            print(f"START GAME #{game_count}")
            continue
        else:
            player_cards += card
            print(f"\nYour card is a {card_name}!")
            print(f"Your hand is: {player_cards}\n")
    else:
        validOption = True

    promptPlayer()
    player_input = int(input(f"Choose an option: "))

    if player_input > 0 and player_input <= 4:
        if player_input == 1:
            continue
        elif player_input == 2:
            dealer_cards = rng.next_int(11) + 16

            print(f"\nDealer's hand: {dealer_cards}")

            if dealer_cards > 21:
                print(f"Your hand is: {player_cards}\n")
                print("You win!\n")

                player_cards = 0
                computer_cards = 0

                game_count += 1
                player_wins += 1

                print(f"START GAME #{game_count}")
                continue
            elif dealer_cards == player_cards:
                print(f"Your hand is: {player_cards}\n")
                print("It's a tie! No one wins!\n")

                player_cards = 0
                computer_cards = 0

                game_count += 1

                print(f"START GAME #{game_count}")
                continue
            else:
                print(f"Your hand is: {player_cards}\n")
                print("Dealer wins!\n")

                player_cards = 0
                computer_cards = 0

                dealer_wins += 1
                game_count += 1

                print(f"START GAME #{game_count}")
                continue
        elif player_input == 3: # player input can only be 3
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {game_count - (player_wins + dealer_wins) - 1}")
            print(f"Total # of games played is: {game_count - 1}")
            print(f"Percentage of Player wins: {((player_wins / (game_count - 1)) * 100):.1f}%\n")

            validOption = False
        else: # player input can only be 4
            break
    else:
        print("Invalid input!\n")
        print("Please enter an integer value between 1 and 4.")

        validOption = False