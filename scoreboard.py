import time

totalscore = 0

def holeone(scoreholeone):
    global totalscore
    totalscore = totalscore + scoreholeone
    return scoreholeone


while True:
    # Take input from the user
    choice = input("Enter hole number (1, 2, 3, 4, 5)")
    if choice in ('1', '2', '3', '4', '5'):
        holescore = int(input("score for the hole:"))
        if choice == '1':
            print("your score is:", holeone(holescore), "for hole number", choice)
            time.sleep(1.5)
            print("your total score is:", totalscore)
    # break
