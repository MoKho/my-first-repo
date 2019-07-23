import random
UnderstandableAnswers = ["yes", "y", "Y", "Yes", "YES", "No", "n", "N", "NO", "no"]
OkayAnswers = UnderstandableAnswers[:5]
anothertry = "yes"
while anothertry in OkayAnswers :
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    print ("1st dice: ", x1, "\n2nd dice: ", x2)
    if x1 > x2 :
        print("\nobviously the 1st one wins this match")
    else:
        print("\nobviously the 2nd one wins this match")
    i = True
    while i :
        anothertry = input("wanna try again?(y/n)")
        if anothertry in UnderstandableAnswers :
            i = False
        else:
            print("\nI can't understand you")
            i = True


print ("Bye bye...")