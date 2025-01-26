import random

#The following function gets a random number from 1 to 9
def get_random_card():
    return random.randrange(1, 10)

#The following function receives 3 parameters and calculates the total
def bob(a, b, c):
    return a + b + c
    bobtotal=a+b+c

#The following function receives 3 parameters and calculates the total
def player(a, b, c):
    return a + b + c
    playertotal=a+b+c

#The following function receives 3 parameters and calculates the total
def james(a, b, c):
    return a + b + c
    jamestotal-a+b+c

#The following function introduces the game to the user
def intro():
    print("Welcome to COMBO 12!")
    print("Your goal is to ultimately get a set of number cards totaling 12")
    print("Your fellow players are Bob and James")
    print("Now that we are all set, let's get started!\n")

#The following function does the processes involved in a round of the game
def game():

    playercard1 = get_random_card()
    playercard2 = get_random_card()
    playercard3 = get_random_card()

    player1card1 = get_random_card()
    player1card2 = get_random_card()
    player1card3 = get_random_card()

    player2card1 = get_random_card()
    player2card2 = get_random_card()
    player2card3 = get_random_card()
    #Assigns an inital value to all of the cards of the 3 players

    playertotal = player(playercard1, playercard2, playercard3)
    #Runs the player function to get the total for the first round output

    print("Your cards are",playercard1,playercard2,playercard3,"with a total of",playertotal,)
    #Outputs player information for the first turn

    player1total = bob(player1card1, player1card2, player1card3)
    playertotal = player(playercard1, playercard2, playercard3)
    player2total = james(player2card1, player2card2, player2card3)
    #Calculates card total for all players

    while(player1total!=12)and(playertotal!=12)and(player2total!=12):
    #Repeats turns until a player wins (gets a set of cards totaling 12)

        playercard1 = get_random_card()
        playercard2 = get_random_card()
        playercard3 = get_random_card()

        player1card1 = get_random_card()
        player1card2 = get_random_card()
        player1card3 = get_random_card()

        player2card1 = get_random_card()
        player2card2 = get_random_card()
        player2card3 = get_random_card()
        #Updates each players set of cards each turn

        player1total = bob(player1card1, player1card2, player1card3)
        playertotal = player(playercard1, playercard2, playercard3)
        player2total = james(player2card1, player2card2, player2card3)
        #Calculates updated total for the players using functions

        print("Your cards are",playercard1,playercard2,playercard3,"with a total of",playertotal,)
        #Prints turn information

    if playertotal == 12:
        print("DOUZE! Congratulations! You win!\n")
    elif player1total == 12:
        print("DOUZE! Bob won, you lose\n")
    elif player2total == 12:
        print("DOUZE! James won, you lose\n")
        #Determines the winner (checks who's cards total 12)


 return(playertotal)

#The following function repeats the game 50 times and keeps track of how many wins
def totalwins():

    winnum = 0
    #Creates a variable for total number of wins

    for c in range(50):
        #repeats game 50 times
        result=game()
        #Creates a variable to store the game function and run it
        if(result==12):
            #Checks if the value in game is 12 (sees if the user won)
            winnum=winnum+1
            #If so adds 1 to the total number of wins

    print("You won", winnum, "times out of 50")
    #Outputs the total number of wins out of 50

intro()
totalwins()
#Calls the functions intro and totalwins

