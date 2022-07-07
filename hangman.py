import random

def hangman(word):
    wrong=0
    stages=["",
            "_________       ",
            "|               ",
            "|       |       ",
            "|       O       ",
            "|      /|\      ",
            "|      / \      ",
            "|               "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to HANGMAN")
    while wrong<len(stages)-1:
        print("\n")
        msg="guess a letter"
        char=input(msg)
        if char in  rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:]))
        print("you lose! The answer is {}".format(word))


lists=["tomoko","yoshiki","kida","Kyoto","Tokyo","Osaka"]

number=random.randint(0,len(lists)-1)
word1=lists[number]
hangman(word1)
