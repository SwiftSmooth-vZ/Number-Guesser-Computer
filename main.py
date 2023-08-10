import random
print("Hello and Welcome to this Number guessing game.")
print("The Computer will generate a number between a mentioned specified range.")
print("If you correctly guess the number 10 times you win, otherwise if you fail to guess 10 times you lose.")
print("Remember to input an integer value only.")
print("Good Luck and let's get started")

range1 = None
range2 = None
win_count = 0
lose_count = 0
condition = True
while condition == True:
    range_start = int(input("Please type in your starting range: "))
    range_finish = int(input("Please type in your end range (make sure it's bigger than the the starting range): "))
    if range_finish > range_start:
        condition = False
    else:
        print("Invalid range please try again")
while win_count < 10 and lose_count < 10:
    if range_finish > range_start:
        random_num = random.randint(range_start, range_finish)
        choice = int(input(f"Please guess the number between (or including) the range {range_start} and {range_finish}: "))
        if choice == random_num:
            print("\nCongratulations, you guessed the number correctly, move on to the next guessing session")
            win_count += 1
        else:
            print("Oops, seems as though your inputted number or string isn't correct. Please try again")
            lose_count += 1
if win_count == 10:
    print(f"Congratulations on winning. You have correctly guessed 10 numbers and incorrectly guessed {lose_count} numbers.")
    print("Thank you for playing this game")
else:
    print(f"Unfortunately you lost. It was a good try though, you managed to get {win_count} number(s) correctly. Keep trying.")
