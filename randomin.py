'''import random
def guess_no():
    return random.randint(1,100)

target_no=guess_no()
attempts=0

while True:
    user_guess=int(input("guess the number:"))
    attempts+=1
    if user_guess==target_no:
        print("congrats you guess right",attempts,"attempt")
    elif user_guess<target_no:
        print("try higher no.")
    else:
        print("try lower no.")'''



