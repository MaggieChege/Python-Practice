import sys
shikoh = raw_input("Shiko:         Choose rock, paper or scissors\n")
shiroh = raw_input("Shiro:         Choose rock, paper or scissors\n")


def player(shiko, shiro):
    shiko = shikoh
    shiro = shiroh

    if shiko == "rock" and shiro == "rock":
        print("thats a tie")
    elif shiko == "rock" and shiro == "paper":
         print("Shikoh wins")
    elif shiko == "rock" and shiro == "scissors":
        print("Shikoh wins")
    elif shiko == "paper" and shiro == "rock":
        print("Shiro wins")
    elif shiko == "scissors" and shiro == "rock":
        print("Shiro wins")
    #this closes the a program
    elif "exit":
        sys.exit(1)
    else:
        print("SHIRO wins")

player(shikoh,shiroh)