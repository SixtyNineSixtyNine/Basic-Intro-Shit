print("Welcome do da club bitches, let's do a quiz")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()
    
print("K BLESS UP LES PLAY")

score = 0
#_______________________________
answer = input("What is the short form of central processing unit ")
if answer.lower() == "cpu":
    
    print("CORRECT")
    score += 1
else:
    print("WRONG")

#_______________________________
answer = input("What is the short form of graphics processing unit ")
if answer.lower() == "gpu":
    
    print("CORRECT")
    score += 1
else:
    print("WRONG")

#_______________________________
answer = input("Which cardinal direction does the sun rise from ")
if answer.lower() == "east":
    
    print("CORRECT")
    score += 1
else:
    print("WRONG")

#_______________________________
answer = input("Which side does it set ")
if answer.lower() == "west":
    
    print("CORRECT")
    score += 1
else:
    print("WRONG")

print(score)
#_______________________________
if score >2:
    print("You got " + str(score) + " questions correct, You're the best. No one makes me laugh as much as and feel as happy, or even feel as beautiful as you do. You help me feel like I can do anything. ")
else:
    print("You got " + str(score) + " questions correct, Everything happens for a reason. Sometimes the reason is you're stupid and make bad decisions. Just because we accept you as you are doesn’t mean we’ve abandoned hope you’ll improve.")
 
