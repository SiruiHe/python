import random
guess=""
while guess not in ("heads","tails"):
    print("Enter heads or tails:")
    guess=input()
toss=random.randint(0,1)
list=["heads","tails"]
toss=list[toss]
if toss==guess:
    print("You got it")
else:
    print("Nope!Try again!")
    guesss=input()
    if toss==guesss:
        print("You got it")
    else:
        print("NOPE.SO BAD!")