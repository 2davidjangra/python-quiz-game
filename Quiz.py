print("Welcome To The Quiz ")

Playing  = input("Do You Want To Play The Quiz ")

if(Playing  != "yes"):
    quit()

print("Let's Ready To Play The Quiz \n")

score = 0

Que1 = input("What is The Full Form CPU ")
Ans1 = "central processing unit"

if(Que1.lower() == Ans1):
    print("Corret! ")
    score +=1
else:
    print("Incorrect")

Que2 = input("What is The Full Form GPU ")
Ans2 = "graphical processing unit"

if(Que2.lower() == Ans2):
    print("Corret! ")
    score +=1
else:
    print("Incorrect")

Que3 = input("What is The Full Form WWW ")
Ans3 = "world wide web"

if(Que3.lower() == Ans3):
    print("Corret! ")
    score +=1
else:
    print("Incorrect")

Que4 = input("What is The Full Form LAN ")
Ans4 = "local area network"

if(Que4.lower() == Ans4):
    print("Corret! ")
    score +=1
else:
    print("Incorrect")

print("Your Score Is ",score)
print("The Percentange You Got ", (score/4)*100)
