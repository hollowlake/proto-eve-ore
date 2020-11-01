# This program will ask three questions and give a calculation based on those answers.
import json

while True:

    with open('./ore.json') as json_file:
        ores = json.load(json_file)

    oreVal = input("\nWhat ore are you transporting? \n").lower()
    oreCom = input("\nIs it compressed?\n").lower()
    oreCar = int(input("\nHow much space is available?\n"))

    try:
        if oreCom == "yes":
            oreCom = ores[oreVal]["compressed"]

        if oreCom == "no":
            oreCom = ores[oreVal]["uncompressed"]

        result = int(oreCar/oreCom)

        print(f'\nName: {oreVal.title()} | Specified Size: {oreCom}m3')
        print(f'You can carry {result}m3 {oreVal.title()} in a ship with {oreCar}m3 available!')

    except:
        print(f"\nStrange, that didn't work. Check your entries and try again!")

    while True:
        answer = str(input('\nDo you need another run? \n'))
        if answer in ('yes', 'no', 'y', 'n'):
            break
        print("invalid")

    if answer == "yes" or answer == "y":
        continue

    else:
        print("\nSee ya!")
        break
