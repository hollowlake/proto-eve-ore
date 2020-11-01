# This program will ask three questions and give a calculation based on those answers.
import json
while True:

    with open('./ore.json') as json_file:
        data = json.load(json_file)

    oreVal = data[input("What ore are you transporting? \n").lower()]
    oreCom = input("\nIs it compressed?\n").lower()
    oreCar = int(input("\nHow much space is available?\n"))

    if oreCom == "yes":
        oreCom = oreVal["compressed"]

    if oreCom == "no":
        oreCom = oreVal["uncompressed"]

    result = int(oreCar/oreCom)

    print("%2f", result)

    while True:
        answer = str(input('Run again? \n'))
        if answer in ('yes', 'no', 'y', 'n'):
            break
        print("invalid")
    if answer == "yes" or answer == "y":
        continue
    else:
        print("\nSee ya!")
        break
