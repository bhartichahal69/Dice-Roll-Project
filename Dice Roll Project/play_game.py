import random
def play():
    print("\n Starting Dice Game\n")
    input("Player 1 press Enter to roll")
    p1 = random.randint(1,6)
    print("Player 1 rolled:",p1)
    input("Player 2 press Enter to roll")
    p2 = random.randint(1,6)
    print("Player 2 rolled:",p2)
    
    if p1>p2:
        print("Player 1 Wins!")
    elif p2>p1:
        print("Player2 Wins!")
    else:
        print("It's a Tie!")
