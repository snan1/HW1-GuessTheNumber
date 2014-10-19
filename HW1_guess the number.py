#Sidharth Sudhakar Nandury
#Homework 1
#Guessing the number
#Date: 12th Sept 2014




replay='y'

while (replay=='y'):
    max=100
    min=0
    mid=((max+min)//2)
    attempts=0
    name=input("Hi! What's your name?")
    print("Hi {:s}! Let's play a game! Chose any number netween 1-100 and I'll try to guess it!".format(name))
    guess=input("Is the number {:d}? (yes/no)".format(mid))
    attempts=attempts+1

    if (guess=='yes'):
        print("Wow!I guessed it in {:d} attempts. I must be smart!".format(attempts))

    greater=input("Is the number greater than {:d}?(Yes/No)?".format(mid))

    while (guess=='no' and (greater=='yes' or greater=='no')):
        while (greater=="yes"):
            min=mid+1
            mid=((max+min)//2)
            guess=input("Is the number {:d}? (Yes/No)".format(mid))
            if (guess=='no'):
                attempts=attempts+1
                greater=input("Is the number greater than {:d}?(Yes/No)?".format(mid))
            elif(guess=='yes'):
                attempts=attempts+1
                print("Wow!I guessed it in {:d} attempts. I must be smart!".format(attempts))
                break

        while (greater=="no"):
            max=mid-1
            mid=((max+min)//2)
            guess=input("Is the number {:d}? (Yes/No)".format(mid))
            if (guess=='no'):
                attempts=attempts+1
                greater=input("Is the number greater than {:d}?(Yes/No)?".format(mid))
            elif(guess=='yes'):
                attempts=attempts+1
                print("Wow!I guessed it in {:d} attempts. I must be smart!".format(attempts))
                break

    replay=input("Did you have fun? Wanna play again?\n Y or N?")
    
                
            
        
             
    
