# Program to determine how much ore a specified amount of cargo space can hold
# More or less a pointless practice program

import json

# keeps program running until manually closed
while True:

    with open('./ore.json') as json_file:
        ores = json.load(json_file)

    # standard input variables / lower() to allow reading capitalization
    oreVal = input("\nWhat ore are you transporting? \n").lower()
    oreCom = input("\nIs it compressed?\n").lower()
    oreCar = int(input("\nHow much space is available?\n"))

    # error handling if typo or incorrect entries
    try:
        # takes user input and converts it to required json keys
        if oreCom == "yes":
            oreCom = ores[oreVal]["compressed"]

        if oreCom == "no":
            oreCom = ores[oreVal]["uncompressed"]

        # divides cargo space by ore size to determine allowed volume
        result = int(oreCar/oreCom)

        # prints selected variables
        print(f'\nName: {oreVal.title()} | Specified Size: {oreCom}m3')
        print(f'You can carry {result:,}m3 {oreVal.title()} in a ship with {oreCar}m3 available!')

    except:
        # error message
        print(f"\nStrange, that didn't work. Check your entries and try again!")

    # allows for additional queries
    while True:
        answer = str(input('\nWould you like to do another? \n'))
        if answer in ('yes', 'no', 'y', 'n'):
            break
        print("\nI didn't understand that. Yes or No, please!\n")

    if answer == "yes" or answer == "y":
        continue

    else:
        print("\nThanks for using this program! Come back soon!")
        break
