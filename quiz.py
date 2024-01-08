score=0
print("Welcome to the computer quiz game")
playing=input("would you like to play this game ").lower()
print (playing)
if playing != "yes":
    quit()
else:
    answer=input("what is the full form of cpu ").lower()
    if(answer=="control processing unit"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    answer=input("what is the full form of gpu ").lower()
    if(answer=="graphic processing unit"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("what is the full form of py ").lower()
    if(answer=="python"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    answer=input("what is the full form of cn ").lower()
    if(answer=="cartoon network"):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    print("your scored "+str(score)+" /4")
    print("your scored  "+str((score/4)*100) + " %")
