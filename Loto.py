import random

def lottery(numbers):
    output = []
    for x in range(0, numbers):
        out_number = random.randint(1, 47)
        if out_number not in output:
            output.append(out_number)
        elif out_number in output:
            while out_number in output:
                out_number = random.randint(1, 47)
                if out_number not in output:
                    output.append(out_number)
                    break
    return output

def main():
    while True:

        print "Welcome to my lottery :)"

        try:
            numbers = int(raw_input("Enter how many numbers you want to get (1-47): "))
            if numbers >= 1 and numbers <= 47:
                print lottery(numbers)
            else:
                print "Invalid input"
                continue

            new_game = raw_input("Do you want to get new numbers? (yes/no)").lower()
            if new_game == "yes" or new_game == "y" or new_game == "":
                continue
            else:
                break

        except ValueError:
            print('Invalid input.')

if __name__ == "__main__":
    main()