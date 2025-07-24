def explode_bridgekeeper():
    print("The BridgeKeeper explodes in a blaze of confusion.\n\
        You may cross the bridge.")
    begin_journey()

def begin_journey():
    print("You find yourself standing at the top of a great precipice.  \
        Would you like to:\n\
            A: Jump from the cliff screaming wildly\n\
            B: Sing out and see if your voice echoes\n\
            C: Use your binoculars to see what you can see")
    
    choice = input("What do you choose? ")
    
    if "A" in choice:
        die("You die screaming as your body sails through the clouds.")
    if "B" in choice:
        print("You hear nothing in return except the empty wind.")
        exit(0)
    if "C" in choice:
        paraglider_answer = input("In the distance you see your goal.  Do you open your paraglider?")
        if "yes" in paraglider_answer:
            print("You sail spectacularly to the Cave of Wonders!")
            cave_of_wonders()
        else: 
            "Ummm... nothing happens."
            exit(0)

def cave_of_wonders():
    worthy_ans = input("You arrive at the cave of Wonders.  Are you worthy?")
    if "diamond in the rough" in worthy_ans:
        print("You win all the treasure!")
        exit(0)
    else:
        print("You are eaten by a lion.  The end.")
        exit(0)
    

def die(why):
    print(why)
    exit(0)