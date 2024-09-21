import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to stop the game.")
    
    while True:
        # Ask the user for their choice
        user_choice = input("Your choice: ").lower()
        
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        # Validate user input
        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Generate computer's choice
        computer_choice = random.choice(options)
        
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Run the game
play_game()
