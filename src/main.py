import random


def printIntro():
    print("#  Hello there!")
    print("#  Let us play ROCK-PAPER-SCISSORS")
    print("#  Before we fly, here are some rules of the game.")


def printInstructions():
    print("\t- This game is similar to traditional rock-paper-scissors.")
    print("\t- Except that you are playing with a computer system. (Hi to Me!!)")
    print("\t- At first you will prompted to enter number of rounds you would like to play.")
    print("\t- For each round, you need to enter your choice among Rock-Paper-Scissors")
    print("\t- Pre-assigned integer values of 0,5 and 2 can be used for rock paper and scissors respectively.")
    print("\t- Or else just type in the word in english language, in lower or upper or mixed case.")
    print("\t- Don't worry about the typing errors.Just make sure first letter is relevant to your choice.")
    print("\t- Computer will make its own choice regarding which it is assured that choice will not be biased towards winning.")
    print("\t- The game shows no mercy. If you violate the rules, you have to start over again.")
    print("\t- GOOD LUCK!\n")


def formatInput(player):
    if(player[0].isdigit()):
        try:
            temp = int(player)
            if(temp == 2 or temp == 5 or temp == 0):
                return temp
            raise ValueError
        except ValueError:
            print("#  Enter valid input. Check these instructions and restart the game.\n")
            printInstructions()
            exit()


    player = player.lower()
    if(player[0] == 'r'):
        return 0
    if(player[0] == 'p'):
        return 5
    if(player[0] == 's'):
        return 2


def makeRandomChoice():
    return random.choice([0, 2, 5])


def judgeCurrentGame(player, system, humanScore, computerScore):
    if(player == system):
        print("\tDraw")
    elif(player == 0):
        if(system == 2):
            print("\tPLAYER: ROCK\tSYSTEM: SCISSORS")
            print("\tRock breaks Scissors. I lost. Awww..")
            humanScore += 1
        else:
            print("\tPLAYER: ROCK\tSYSTEM: PAPER")
            print("\tPaper wraps Rock. I just beat you.")
            computerScore += 1
    elif(player == 2):
        if(system == 5):
            print("\tPLAYER: SCISSORS\tSYSTEM:PAPER")
            print("\tYour Scissors cut through my paper. You beat me.!")
            humanScore += 1
        else:
            print("\tPLAYER: SCISSORS\tSYSTEM:ROCK")
            print(
                "\tYou know rocks are strong enough to break scissors! Oh yes, you lost")
            computerScore += 1
    else:
        if(system == 0):
            print("\tPLAYER: PAPER\t SYSTEM: ROCK")
            print("\tPaper wraps rock. Aww.. I lost ")
            humanScore += 1
        else:
            print("\tPLAYER: PAPER\t SYSTEM: SCISSORS")
            print("\tMy Scissors - Your paper... Chisk..chisk..cut through")
            computerScore += 1
    return humanScore, computerScore


if __name__ == "__main__":
    printIntro()
    printInstructions()
    print(f"# To decide a winner we need fix the total number of rounds we are going to play.")
    totalGames = int(input("# How many rounds would you like to play?\n> "))
    print("> Great Let us start! Something tells me I am gonna win. Anyway let us see!")
    print("")
    gameCount = 1
    humanScore = 0
    computerScore = 0
    while(gameCount <= totalGames):
        print(f"\n> Game: {gameCount}")
        player = (input("  Rock(0) or Paper(5) or Scissors(2)?: "))
        player = formatInput(player)
        system = makeRandomChoice()
        humanScore, computerScore = judgeCurrentGame(
            player, system, humanScore, computerScore)
        gameCount += 1
    print(f"\n# Of the {totalGames} games that we just played,I won {computerScore} and you won {humanScore}.")

    if(humanScore > computerScore):
        print("# Looks like you won! Congrats.I guess I was wrong. Nice playing with you.")
    elif(humanScore < computerScore):
        print("# I won!!\n# Told ya!\n# Anyways, nice playing with you.")
    else:
        print("# We are drawn!")
