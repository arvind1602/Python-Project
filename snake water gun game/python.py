import random

def play_game():
    while True:
        user_choice = input("Enter snake, water, or gun (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            break

        if user_choice not in ['snake', 'water', 'gun']:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(['snake', 'water', 'gun'])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'snake' and computer_choice == 'water') or \
             (user_choice == 'water' and computer_choice == 'gun') or \
             (user_choice == 'gun' and computer_choice == 'snake'):
            print("You win!")
        else:
            print("Computer wins!")

play_game()
