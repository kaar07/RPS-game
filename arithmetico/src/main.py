import random

def printIntro():
    intro = """

    \t    █              ██    ▄   ▀██                           ▄    ██                  
    \t   ███    ▄▄▄ ▄▄  ▄▄▄  ▄██▄   ██ ▄▄   ▄▄ ▄▄ ▄▄     ▄▄▄▄  ▄██▄  ▄▄▄    ▄▄▄▄    ▄▄▄   
    \t  █  ██    ██▀ ▀▀  ██   ██    ██▀ ██   ██ ██ ██  ▄█▄▄▄██  ██    ██  ▄█   ▀▀ ▄█  ▀█▄ 
    \t ▄▀▀▀▀█▄   ██      ██   ██    ██  ██   ██ ██ ██  ██       ██    ██  ██      ██   ██ 
    \t▄█▄  ▄██▄ ▄██▄    ▄██▄  ▀█▄▀ ▄██▄ ██▄ ▄██ ██ ██▄  ▀█▄▄▄▀  ▀█▄▀ ▄██▄  ▀█▄▄▄▀  ▀█▄▄█▀ 
    \t                                                                                
    \t                                                                                
    \tLet us Play!
    \tPress ENTER to start
    """
    print(intro)

def endGame(score,gameCount):
    if(gameCount!=0):
        accuracy = score/gameCount
    else:
        accuracy = 0
    accuracy *= 100
    accuracy = round(accuracy,3)
    print(f"\n\t-> Questions asked:\t{gameCount}")
    print(f"\t-> Correctly answered:\t{score}")
    print(f"\t-> Accuracy:\t{accuracy} %")

def ask():
    operation = random.choice(['+','-','*','/'])

    if(operation == '+'):
        num1 = random.randint(1,100000)
        num2 = random.randint(1,10000)
        rightAns = num1 + num2
    elif(operation == '-'):
        num1 = random.randint(1,100000)
        num2 = random.randint(1,10000)
        rightAns = num1 - num2
    elif(operation == '*'):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        rightAns = num1 * num2
    else:
        num2 = random.randint(1,100)
        factor = random.randint(1,100)
        num1 = num2 * factor
        rightAns = factor
    print(f"\t# Solve this -> {num1} {operation} {num2} :")
    checkAns = input("\t- ")

    try:
        if(int(checkAns) == rightAns):
            print("\t# Right answer!")
            return 1
        else:
            print(f"\t# Wrong Answer! It was {rightAns}")
            return 0
    except ValueError:
        print("\t# The correct answer to all questions are integers. Your answer is wrong.")
        return 0



if __name__ == "__main__":
    printIntro()
    score = 0
    gameCount = 0
    while(True):
        try:
            command = input("\t ")
            if(command == "exit" or command == "quit"):
                endGame(score,gameCount)
                break
            else:
                score+=ask()
                gameCount+=1
            print("\t  Press ENTER to solve next. <C>-c to stop.")
        except KeyboardInterrupt:
            endGame(score,gameCount)
            exit()
