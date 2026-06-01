import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))    #join => take every list join each element by a ""
    print("-------------")

def get_payout(row, bet):
    if row [0] == row [1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 5
        if row[0] == '🍋':
            return bet * 7
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("*********************")
    print("   Welcome Slotter   ")
    print("Symbols : 🍒🍉🍋🔔⭐")
    print("*********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input(f"Place your bet amount: $")

        if not bet.isdigit():
            print("Please enter the valid number")
            continue   #Should we use this? because when no continue it works too..

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue    #again should we?

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")   # What the hell is \n??
        print_row(row)
        print()

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won {payout}")
        else:
            print(f"Sorry you lost this round")
        print()

        balance += payout


if __name__ == "__main__":
    main()