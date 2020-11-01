# This program will ask three questions and give a calculation based on those answers.

while True:

    oreVal = input("\nWhat ore are you transporting? \n")
    oreCom = input("\nIs it compressed?\n")
    oreSpace = int(input("\nHow much space is available?\n"))

    def questions():

        if oreCom == "yes" or oreCom == "y":
            compressed()

            return

        elif oreCom == "no" or oreCom == "n":
            uncompressed()

            return

        else:
            pass

    def uncompressed():

        if "arkonor" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "bezdnacine" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "bistot" in oreVal:

            result = int(oreSpace/4.4)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "crokite" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "gneiss" in oreVal:

            result = int(oreSpace/5)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "hedbergite" in oreVal:

            result = int(oreSpace/3)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "hemorphite" in oreVal:

            result = int(oreSpace/3)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "jaspet" in oreVal:

            result = int(oreSpace/2)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "kernite" in oreVal:

            result = int(oreSpace/0.19)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "mercoxit" in oreVal:

            result = int(oreSpace/0.40)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "ochre" in oreVal:

            result = int(oreSpace/1.2)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "omber" in oreVal:

            result = int(oreSpace/0.6)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "plagioclase" in oreVal:

            result = int(oreSpace/0.35)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "pyroxeres" in oreVal:

            result = int(oreSpace/0.3)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "rakovene" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "scordite" in oreVal:

            result = int(oreSpace/0.15)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "spodumain" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "talassonite" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "veldspar" in oreVal:

            result = int(oreSpace/0.1)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        else:
            pass

    def compressed():

        if "arkonor" in oreVal:

            result = int(oreSpace/8.8)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "bezdnacine" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "bistot" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "crokite" in oreVal:

            result = int(oreSpace/7.81)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "gneiss" in oreVal:

            result = int(oreSpace/1.8)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "hedbergite" in oreVal:

            result = int(oreSpace/0.47)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "hemorphite" in oreVal:

            result = int(oreSpace/0.86)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "jaspet" in oreVal:

            result = int(oreSpace/0.15)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "kernite" in oreVal:

            result = int(oreSpace/0.19)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "mercoxit" in oreVal:

            result = int(oreSpace/0.1)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "omber" in oreVal:

            result = int(oreSpace/0.3)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "ochre" in oreVal:

            result = int(oreSpace/4.2)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "plagioclase" in oreVal:

            result = int(oreSpace/0.15)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "pyroxeres" in oreVal:

            result = int(oreSpace/0.16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "rakovene" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available.\n')

        if "scordite" in oreVal:

            result = int(oreSpace/0.19)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "spodumain" in oreVal:

            result = int(oreSpace/28)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "talassonite" in oreVal:

            result = int(oreSpace/16)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        if "veldspar" in oreVal:

            result = int(oreSpace/0.15)
            print('\nYou can transport {:,}'.format(result), f'units in a ship with {oreSpace}m3 of space available. \n')

        else:
            pass


    questions()

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
