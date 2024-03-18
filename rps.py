import random
while True:
    print("Hey! Welcome to Rock Paper Scissors")
    
    def win(comp, user):
        stat = "undefined"
        if user == comp:
            stat = "It's a tie!"
        elif user == 1:
            if comp == 3:
                stat = "You win!"
            else:
                stat = "You lose!"
        elif user == 2:
            if comp == 1:
                stat = "You win!"
            else:
                stat = "You lose!"
        elif user == 3:
            if comp == 2:
                stat = "You win!"
            else:
                stat = "You lose!"
        print(stat)
        return 0

    print("Enter your choice: \n1. rock \n2. paper \n3. scissors")
    ch = int(input("Enter your choice: "))
    comp = random.randint(1, 3)
    win(ch, comp)