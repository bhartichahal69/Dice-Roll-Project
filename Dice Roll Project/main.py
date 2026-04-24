from play_game import play
from exit_game import exit_game
while True:
    print("\n===Dice Game menu===")
    print("1.Play Game")
    print("2.Exit Game")

    choice = input("Enter your choice")
    if choice == '1':
        play()
    elif choice == '2':
        exit_game()
        break
    else:
        print("invalid Choice! Try Again")
        