from cs50 import get_float

cents = 0


def main():
    # Prompt for change
    while True:
        change = get_float("Change owed: ")
        if 0 > change:
            change = get_float("Change owed: ")
        if change > 0:
            break
        return change
    
    # convert change to integer
    cents = round(int(change * 100))
    
    numberOfCoins = 0
    
    # get number of coins
    while cents > 0:
        while cents >= 25:
            numberOfCoins += 1
            cents -= 25
        while cents >= 10:
            numberOfCoins += 1
            cents -= 10
        while cents >= 5:
            numberOfCoins += 1
            cents -= 5
        while cents >= 1:
            numberOfCoins += 1
            cents -= 1
    
    # print number of coins
    print(f"{numberOfCoins}")


# Run programme    
if __name__ == "__main__":
    main()