print("welcome to treasure island.")
print("your mission is to fond the treasure.")
choice1=input('you\'re at a crossroad, where do you want to go?type"left"or "right".').lower()
if choice1 == "left":
    #continue
    choice2=input('you\'re come to a lake. there is an island in middle of the lake.type "wait" to wait for a boat.type "swim" to swim  across.').lower()
    if choice2=="wait":
        choice3=input("you arrive at the island unharmed . there is a house with 3 doors.red ,yellow,blue.which colour do u choose?").lower()
        if choice3=="red":
            print("its a room full of fire.game over")
        elif choice3=="yellow":
            print("you found out a secret door!!!!!!!!!!!")
        choice4=input("there are two unbreakable jars on either side of the secret door.you have to get the key to the door using your hand.choose one jar.jar1 or jar2").lower()
        if choice4=="jar1":
            print("you have got bitten from a dangerous snake.game over")
        elif choice4=="jar2":
            print("you foun out the key .pass through the door.you may find the tresure in it ")
            print("hurray!!!!!!!you found out the treasure!!!")   
        elif choice3=="blue":
            print("you enter into a room  of dangerous chemicals that fell on you.game over ")
        else:
            print("you chose a door that doesnt exist.game over")
    else:
        print("you got attacked by an angry trout.game over.")    

else:
    print("you fell into a hole.Game over.")
    
