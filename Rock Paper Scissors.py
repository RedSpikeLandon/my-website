while True:
    player_one_choice = input("Player One, Rock, Paper, Scissors: ")
    print("\n" * 25)
    player_two_choice = input("Player Two, Rock, Paper, Scissors: ")

 
    if player_one_choice == player_two_choice:
        print("It's a tie")
    elif player_one_choice == "Rock" and player_two_choice == "Paper":
        print("Player_two wins!")
        break
    elif player_one_choice == "Paper" and player_two_choice == "Scissors":
        print("Player_two wins!")
        break
    elif player_one_choice == "Sicissors" and player_two_choice == "Rock":
        print("Player_two wins!")
        break
    elif player_one_choice == "Paper" and player_two_choice == "Scissors":
        print("Player_one wins!")
        break
    elif player_one_choice == "Rock" and player_two_choice == "Paper":
        print("Player_one wins!")
        break
    elif player_one_choice == "Scissors" and player_two_choice == "Rock":
        print("Player_one wins!")
        break
    else:
        print("Choose Rock, Paper, or Scissors.")
