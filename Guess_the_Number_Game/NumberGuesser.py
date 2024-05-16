import random


# function which returns user limit
def limit():
    l =input("Enter the Upper Limit (leave it blank for limit = 100): ").strip()
    return int(l) if l!="" else 100


def takeInput(limit=100):
    i = input(f"Enter your guessed number(1-{limit}): ")
    return int(i) if i!="" else 0

# making a new dialogue function
def dialogue(flag):
    diaList = {
        1:["Its a Big number", "Slightly Big number", "You guessed a large number", "large number", "Higher number", "Too High"],
        2:["Its a Small number", "Slightly Small number", "You guessed a Small number", "Small number", "Lower number", "Too Low"]
    }

    if flag ==1:
        return random.choice(diaList[flag])
    elif flag ==2:
        return random.choice(diaList[flag])


# now making a function which compares user value from cpu generated value in a condition
def isEqual(user,cpu, limit)->bool:
    if user > cpu and 1<=user<=limit:
        flag =1
        print(dialogue(flag))
        return False
    elif user < cpu and 1<=user<=limit:
        flag =2
        print(dialogue(flag))
        return False
    elif user==cpu:
        print("Congratulations! You guessed the right number")
        return True
    else:
        print(f"please guess a number between 1-{limit}")
        return False


user_limit = limit()
cpu = random.randint(1,user_limit)
# print(cpu) #for check (uncomment this line to see the generated value) 

guess = 1
flag = 0

# setting no. of guesses/attempts.
times = 10  # default guess value

while True:

    select = input("LEVELS -> 1-Easy, 2-Normal, 3-Hard: ").strip()
    select = int(select) if select!="" else -1  #checking if the selected option is valid or not?

    if select == 1:
        times = 15 #you can change the value
        print(f"You got {times} chances, Good Luck!")
    elif select == 2:
        times = 8 #you can change the value
        print(f"You got {times} chances, Good Luck!")
    elif select == 3:
        times = 3 #you can change the value
        print(f"You got {times} chances, Good Luck!")

    else:
        print("Invalid choice")
        continue


    # now running the game in a loop

    while times > 0:
        print("Guessed number: ", guess)

        #Making a user input function
        user = takeInput(user_limit)

        if user == 0:
            print("please give a guessed number!")
            continue

        if not isEqual(user,cpu, user_limit):
            flag =1
            times -=1
            guess+=1
        else:
            flag =0
            times -=1
            break

    if flag == 1:
        print("You can't found the right number... Try again")
        break
    else:
        break