import random 
print("welcome to our game ")
def choose():
    words=['APPLE', 'BANANA', 'CARROT', 'DOG', 'ELEPHANT', 'FROG', 'GORILLA', 'HAMMER', 'IGLOO', 'JACKET', 'KANGAROO', 'LION', 'MONKEY', 'OCTOPUS', 'PANDA', 'QUEEN', 'RABBIT', 'SNAKE', 'TIGER', 'UNICORN', 'VOLCANO', 'WHALE', 'XYLOPHONE', 'YELLOW', 'ZEBRA']
    choosed=random.choice(words)
    return choosed
def jumple(word):
    jumpled="".join(random.sample(word,len(word)))
    return jumpled
def thankyou(p1name,p2name,p1,p2):
    print(p1name," your score is " ,p1)
    print(p2name," your score is ", p2)
    if p1>p2:
        print("congratulations ",p1name," you win the game")
    elif p1<p2:
         print("congratulations ",p2name," you win the game")
    else:
        print("Draw")
    print("Thank you ",p1name," and ",p2name," for playing")
    print("Have a nice day :)")
def play():
    p1=0
    p2=0
    p1name=input("player 1 enter your name ")
    p2name=input("player 2 enter your name ")
    count=0
    while(1):
        if((count%2)==0):
            word=choose()
            qn=jumple(word)
            print(qn)
            print(p1name," your turn")
            ans1=input("guess my word ")
            count=count+1
            if ans1.lower()==word.lower():
                p1=p1+1
                print("correct you got 1 point , your total score is ",p1)
            else:
                print("better luck next time.correct answer was ",word)
                
            c=input("if you wish to end the game press 1 else press 2 ")
            c=int(c)
            if(c==1):
                thankyou(p1name,p2name,p1,p2)
                break
            else:
                print()
        else:
            word=choose()
            qn=jumple(word)
            print(qn)
            print(p2name," your turn ")
            ans1=input("guess my word ")
            count=count+1 
            if ans1.lower()==word.lower():
                p2=p2+1
                print("correct you got 1 point , your total score is ",p2)
            else:
                print("better luck next time.correct answer was ",word)
            c=int(input("if you wish to end the game press 1 else press 2 "))
            if(c==1):
                thankyou(p1name,p2name,p1,p2)
                break
            else:
                print()
     
play()            
            
    