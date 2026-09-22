# XORmod (part of the CYBERMATH FOR DUMMIES projecT)
# Copyright (c) 2026 Jacob F. 
# Licensed under the MIT License
# Repository: https://github.com/tenshi-net/cyberMATH_for_Dummies
# This script is a barebones calculator intended for calculating XOR and modulo operations within the command line.

print("\nRunning XORmod for Dummies...")

# This while loop continues running operations until the user opts to exit
while True:
    prompt = input("\nCHOOSE AN OPERATION.\n   OPTIONS: xor, mod, exit \n\n")
    prompt.strip().lower()

    # These if/elif statements are grabbing user input and running either an XOR or modulo operation.
    if prompt == "xor":
        xor_first = int(input("\nEnter the first number: "))
        xor_second = int(input("Enter the second number: "))
        xor_op = xor_first ^ xor_second
        print(f"\nThe result of {xor_first} XOR {xor_second} is {xor_op}.")

        # This block asks the user if they want to continue calculations. If not, the script exits.
        rerun = input("\nDo you want to calculate more? (y/n): ")
        if rerun.lower() == "n":
            print("\nExiting. Re-run the script if you would like to calculate again.\n")
            break
        elif rerun.lower() == "y":
            continue
        else:
            print("Command not recognized. Please re-run the script if you would like to calculate more.")
            break
    elif prompt == "mod":
        mod_first = int(input("\nEnter the first number: "))
        mod_second = int(input("Enter the second number: "))
        mod_op = mod_first % mod_second
        print(f"\nThe result of {mod_first} mod {mod_second} is {mod_op}.")

        # Similar to the related code in the XOR segment, this asks if the user wants to continue calculating.
        rerun = input("\nDo you want to calculate more? (y/n): ")
        if rerun.lower() == "n":
            print("\nExiting. Re-run the script if you would like to calculate again.\n")
            break
        elif rerun.lower() == "y":
            continue
        else:
            print("Command not recognized. Please re-run the script if you would like to calculate more.")
            break
    elif prompt == "exit":
        print("Exiting. Re-run the script if you would like to calculate more.\n")
        break
    else:
        print("Not a valid operation. Choose either 'xor' or 'mod'.")
