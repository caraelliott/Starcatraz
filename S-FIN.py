import time

print("")
print(" __,  _,  _,  _, __, __,   __, __,  _, _, _    _, ___  _, __,  _,  _, ___ __,  _, ___,")
print(" |_  (_  / ` /_\ |_) |_    |_  |_) / \ |\/|   (_   |  /_\ |_) / ` /_\  |  |_) /_\ ` /") 
print(" |   , ) \ , | | |   |     |   | \ \ / |  |   , )  |  | | | \ \ , | |  |  | \ | |  /")  
print(" ~~~  ~   ~  ~ ~ ~   ~~~   ~   ~ ~  ~  ~  ~    ~   ~  ~ ~ ~ ~  ~  ~ ~  ~  ~ ~ ~ ~ ~~~")                                                                                                                                                  
print("")   
print("")
answer_A = ["A","a"]
answer_B = ["B","b"]
answer_C = ["C","c"]
answer_Yes = ["Yes","yes","y","YES"]
answer_No = ["No","no","n","NO"]
alive = True
required = ("\nUse only A, B, or C\n")

def game():
    print ("You have awoken in a small prison cell.")
    print("There is a sign in the distance saying 'Starcatraz Maximum Security Prison'.")
    print ("A booming voice comes from your cell,")
    print ("'You've finally woken up, you've been out of it for days.")
    print("You're'the first cellmate I've had in years...")
    print("What star system are you from?'")
    print("")
    level_one()

def game_over (alive):
    if alive == True:
        print("SUCCESS!")
        print("Congratulations! You escaped Starcatraz unscathed!")
        print("You vow to ditch your criminal ways now that you have a new shot at life...")
        print("")
        print("")
        print("THE END")
        print("")
        print("Play again?")
        if answer_Yes:
            game()
            print ("")
        #print("A. Promixma Centuri")
        #print("B. Sol")
        #print("C. Arctaurus")
            print("")
            choice = input (str(">>>   "))
        else:
            print ("Until next time...")
            print("")
    if alive == False:
        print ("You have failed, would you like to play again?")
        input ()
        print("")
    if answer_Yes:
        game()
        print ("")
        #print("A. Promixma Centuri")
        #print("B. Sol")
        #print("C. Arctaurus")
        print("")
        choice = input (str(">>>   "))
    else:
        print ("Until next time, inmate...")
        print("")

def level_one():
    print("A. Promixma Centuri")
    print("B. Sol")
    print("C. Arctaurus")
    print("")
    choice = input(str(">>>   "))

    if choice in answer_A:
            print ("You Centuri scum! Your people killed everyone I ever knew!")
            print ("Your cellmate grabs a shank from under his pillow and kills you")
            print("GAME OVER!!!")
            print("")
            alive = False
            game_over(alive)
    elif choice in answer_B:
            print ("You're way out your depth, man! This is what happens when humans play with space travel...")
            NAME=str(input("What is your name?: "))
            print ("Well",NAME, "you're gonna have the time of your life in Starcatraz...")
            option_Sol()
    elif choice in answer_C:
            print ("Ahh, a fellow Arctarian, I shoulda known.")
            NAME=str(input("What is your name, friend?: "))
            print ("Well",NAME, "you're in Starcatraz now...")
            option_Arctaurus()


def option_Sol():
    print("'Right, well now that the introductions are done with,")
    print("how do you suggest we get out of here?'")
    print("")
    print("Do you:")
    print("A: Look Left")
    print("B: Look Right")
    print("")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("Aha!")
        print("You see a ventilation shaft.")
        print("")
        option_Shaft()
    elif choice in answer_B:
        print("You see through the bars that there is a Datapad on a desk nearby")
        print("and a dead animal in the corner of the cell")
        print("")
        option_Breakout()


def option_Shaft():
    print("After closer inspection, the ventilation shaft looks pretty small.")
    print("There is no way your cellmate is gonna fit through there!")
    print("Do you leave him behind?")
    print("A: Abandon cellmate and squeeze through the ventilation shaft alone")
    print("B: Try something else, it's best to stick together")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("Success!")
        print("You have escaped!")
        print("Time to get out of this Godforsaken prison!")
        print("You look around.")
        option_Go()
    if choice in answer_B:
        option_Sol()
        choice = input (str(">>>   "))
def option_Arctaurus():
    print("'Let's get out of here!")
    print("You see that Datapad there?")
    print("I can reach it if you cause a distraction...'")
    print("")
    print("You see through the bars that there is a Datapad on a desk nearby")
    print("and a dead animal in the corner of the cell")
    print("")
    option_Breakout()

def option_Breakout():
    print("")
    print("Do you:")
    print("A: Pick up dead animal")
    print("B: Try to reach the Datapad")
    print("C: Try something else")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You throw the dead animal as a distraction.")
        print("Your cell mate extends his cybernatic arm")
        print("and grabs the Datapad!")
        print("")
        print("")
        print("You see that the Datapad is a key system")
        print("and can be used to unlock the cells.")
        print("")
        option_UnlockAttempt()
    if choice in answer_B:
        print("Oh no!")
        print("A guard sees you,")
        print("and shoots you before you can reach the Datapad!")
        print("")
        print("You died!")
        print("GAME OVER!")
        print("")    
        alive = False
        game_over(alive)
    if choice in answer_C:
        option_Breakout()
  

def option_Go():
    print("To your LEFT is a Guard Tower.")
    print("To your RIGHT is the Main Corridor.")
    print("")
    print("Do you: ")
    print("A: Go Left")
    print("B: Go Right")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You go towards the general direction of the Guard Tower.")
        print("You notice there is a Bookshelf along the corridor wall.")
        print("Further down the corridor is the Guard Tower itself")
        corridor()
    elif choice in answer_B:
        print("You go towards the Main Corridor.")
        print("It goes past cell-blocks filled with sleeping inmates")
        main_corridor()

def corridor():
    print("Do you: ")
    print("A: Inspect the Bookcase")
    print("B: Go to the Guard Tower")
    choice = input (str(">>>   "))
    if choice in answer_A:
        print("You inspect the Bookcase and have a look at the books it holds.")
        print("Two books pique your interest")
        print("One of them is in indecipherable alien characters, but just stands out to you")
        print("The other is ''How to Escape Prison for Dummies''...")
        option_Books()
    elif choice in answer_B:
        print("You walk towards the Guard Tower")
        print("Are you sure you thought this through? It's full of guards!")
        print("Guards spot you and shoot you on sight, they're not taking any chances!")
        print("...")
        print("You die instantly.")
        print("GAME OVER!")
        alive==False
        game_over(alive)


def option_Books():
    print("Do you: ")
    print("A: Take a closer look at [REDACTED]")
    print("B: Grab ''How to Escape Prison for Dummies''")
    choice = input (str(">>>   "))
    if choice in answer_A:
        print("Despite the book being unreadable, you scan the front and back pages.")
        print("You may as well have a look inside, while you're at it.")
        print("A Note falls out!")
        print("The Note details the route to the Warden's Office:")
        print("''Through the main corridor is where the Warden resides, as does his Escape Pod- Good Luck!''")
        print("Wow! What a hunch!")
        option_Go()
    elif choice in answer_B:
        print("You pick up ''How to Escape Prison for Dummies")
        print("Unfortunately, life is never that easy!")
        print("The book unsurprisingly contains no helpful suggestions.")
        print("")
        print("")
        print("")
        option_Go()

def main_corridor():
    print("Do you: ")
    print("A: Continue down the main corridor")
    print("B: Go back")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You see a Cleaning Closet further down the corridor as well as the Warden's Office")
        further_Down_Corridor()
    if choice in answer_B:
        option_Go()

def further_Down_Corridor():
    print("Do you: ")
    print("A: Head towards the Warden's Office")
    print("B: Have a look in the Cleaning Closet")
    print("")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You decide to risk it and go to the Warden's Office")
        option_Warden()
    elif choice in answer_B:
        print("You decide that time is not of the essence and look in the Cleaning Closet")
        option_Closet()

def option_Warden():
    print("Inside the Warden's Office, you see a Desk, a Window and a Display Case")
    print("")
    print("Do you: ")
    print("A: Take a further look at the Warden's desk")
    print("B: Go towards the Window")
    print("C: Have a gander at the Warden's Display Case. Why not have a nosey?")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You walk up to the Warden's Desk")
        print("Now that you're standing up close and personal, you peek at what is on top of the desk")
        print("You figure you may as well look inside the drawers too.")
        option_Desk()
    elif choice in answer_B:
        print("You look out of the porthole and notice an Escape Pod")
        print("This could be the getaway plan you've been looking for!")
        print("Uh oh!")
        print("...")
        print("On closer inspection, you notice that it only has room for one person!")
        option_Warden()
    elif choice in answer_C:
        print("You tentatively take a look at the display case.")
        print("Now that you've had a good look, you realise there is a Laser Sword inside!")
        option_Case()

def option_Case():
    print("Do you attempt to open the Display Case to get to the contents?")
    print("A: Yes")
    print("B: No")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("Oh no!")
        print("...")
        print("An Alarm sounds. Instantly the Warden's Office is flooded with Guards!")
        print("You have no weapons and you are shot dead by Guards")
        print("You are killed instantly!")
        print("GAME OVER!")
        alive==False
        game_over(alive)
    elif choice in answer_B:
        option_Warden()


def option_Desk():
    print("On top of the Desk is the Warden's personal Computer Terminal.")
    print("In the Drawer, there is a Small Box")
    print("Do you: ")
    print("A: Try to hack the Computer Terminal")
    print("B: Look inside the Small Box from the Warden's Drawer?")
    choice = input (str(">>>   "))

    if choice in answer_A:
        option_Hack()
    elif choice in answer_B:
        option_Box()

def option_Hack():
    print("You've seen enough movies to think you know what you're doing")
    print("You attempt to Hack the Terminal...")
    print("Oh no!")
    print("...")
    print("An Alarm sounds. Instantly the Warden's Office is flooded with Guards!")
    print("You have no weapons and you are shot dead by Guards")
    print("You are killed instantly!")
    print("GAME OVER!")
    alive==False
    game_over(alive)


def option_Box():
    print("You rifle through the Small Box,")
    print("noticing a small family photograph and some keys.")
    print("You notice that the photograph has what appears to be a Password scrawled on the back!")
    print("Feeling lucky, you try the Password on the Computer Terminal and it works!")
    print("You have a root around on the Interface and click on ''Contingency Plan''")
    print("Hooray! This unlocks an Escape Pod! It must be your lucky day.")
    option_Password_Accepted()

def option_Password_Accepted():
    print("Oh no, an Alarm starts sounding!")
    print("Guess you're never too lucky.")
    print("")
    option_Alarm()

def option_Alarm():
    print("Do you: ")
    print("A: Head straight for the Escape Pod, there's no time to deal with the Alarm!")
    print("B: Use the newly-found Password to stop the Alarm from the Terminal")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You run for the Escape Pod, feeling the pressure from the Alarm!")
        print("The Guards manage to catch up to you, thanks to the head start from the blaring Alarm")
        print("Your Escape Pod is shot down and your escape mission fails!")
        print("You died!")
        print("GAME OVER!")
        alive==False
        game_over(alive)
    elif choice in answer_B:
        print("You go back onto the Warden's Terminal and disable the alarm before it rings for too long.")
        print("Maybe the guards will think it was a false alarm, or slept through it.")
        print("You get in the Escape Pod and speed off like there's no tomorrow!")
        alive==True
        game_over(alive)

def option_Closet():
    print("In the cleaning closet, you take a look around.")
    print("You notice a Lock Box with a flimsy padlock on the floor, a Spanner on the shelf and a Mop Bucket in the corner.")
    print("Do you:")
    print("A: Take a further look at the Locked Box")
    print("B: Grab the Spanner from the shelf")
    print("C: Look in the Mop Bucket")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("Upon closer inspection, it's locked tight!")
        print("Although flimsy, you aren't strong enough to break the lock with your bare hands.")
        print("Maybe you could find something to pry it open with...")
        print("")
        print("")
        print("")
        further_Down_Corridor()
        print("")
        print("")
        print("")
    elif choice in answer_B:
        print("You grab the spanner! It could be used for self defence, if not for the heavily armed guards...")
        print("It also might be useful for brute force if necessary to aid your escape!")
        spanner = 1
        further_Down_Corridor()
        print("")
        print("")
        print("")
    elif choice in answer_C:
        print("You get closer to the Mop Bucket...")
        print("For some reason...")
        print("As expected, you find nothing of interest.")
        further_Down_Corridor()
        print("")
        print("")
        print("")

def corridor():    
        print("Do you: ")
        print("A: Take a closer look at the books on the bookshelf")
        print("B: Head towards the Guard Tower and go in")
        choice = input (str(">>>   "))
        if choice in answer_A:
            print("You inspect the Bookcase and have a look at the books it holds.")
            print("Two books pique your interest")
            print("One of them is in indecipherable alien characters, but just stands out to you")
            print("The other is ''How to Escape Prison for Dummies''...")
            option_Books()
        elif choice in answer_B:
            print("You walk towards the Guard Tower")
            print("Are you sure you thought this through? It's full of guards!")
            print("Guards spot you and shoot you on sight, they're not taking any chances!")
            print("...")
            print("You die instantly.")
            print("GAME OVER!")
            alive==False
            game_over(alive)
            print("")
            print("")
            print("")

def option_UnlockAttempt():
    print("Do You: ")
    print("A: Unlock just your own cell")
    print("B: Unlock all the cells")
    print("")
    choice = input (str(">>>   "))

    if choice in answer_A:
        print("You unlock your own cell.")
        print("You have escaped!")
        print("Time to get out of this Godforsaken prison!")
        print("You look around.")
        option_Go()
    elif choice in answer_B:
        print("You unlock all cells.")
        print("The other inmates start a stampede!")
        print("You and your cellmate are crushed in the frenzy.")
        print("")
        print("You died!")
        print("")
        print("GAME OVER!")
        alive==False
        game_over(alive)


game()

    

