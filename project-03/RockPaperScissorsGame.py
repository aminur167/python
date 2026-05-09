import random

print("🎮 Welcome to Rock Paper Scissors Game!")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper or scissors (or 'exit' to quit): ").lower()

    if user == "exit":
        print("👋 Thanks for playing!")
        break

    if user not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"🖥 Computer chose: {computer}")

    if user == computer:
        print("🤝 Draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")

    print("-" * 30)