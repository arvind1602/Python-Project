import random

computer_choose = random.randrange(1,100)
print(computer_choose)
count = 1

for i in range( 1 , 7):
    user_choose = int(input('guess the number : '))
    
    if computer_choose == user_choose :
        print(f"user guess right number in {count} time")
        break

    elif computer_choose > user_choose :
        print("user guess too low")

    else :
        print("user guess too high")
    
    count += 1

if count == 7 : print("user cross the limit ")
