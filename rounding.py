#!/usr/bin/env python3
# Created By: Finn Kitor
# Date: December 4th, 2023
# This program rounds a number with any decimal places the user inputs

def round_decimal(decimal_number, num_decimal_places):
    # Checking if the decimal_number parameter is a valid float
    if not isinstance(decimal_number, float):
        raise ValueError("Invalid decimal number. Please provide a valid float.")

    # Checking if the num_decimal_places parameter is a valid integer
    if not isinstance(num_decimal_places, int):
        raise ValueError(
            "Invalid number of decimal places. Please provide a valid integer."
        )

    # Rounding the decimal number to the given number of decimal places
    multiplier = 10**num_decimal_places
    decimal_number *= multiplier
    decimal_number = int(decimal_number + 0.5)
    decimal_number /= multiplier


def main():
    try:
        # Getting user input for the decimal number
        decimal_number = float(input("Enter a decimal number: "))

        # Getting user input for the number of decimal places to round
        num_decimal_places = int(
            input("Enter the number of decimal places to round to: ")
        )

        # Rounding the decimal number
        round_decimal(decimal_number, num_decimal_places)

        # Printing the rounded decimal number
        print(f"The rounded decimal number is: {decimal_number}")

    except ValueError as e:
        print(f"Invalid input: {e}")


# Calling the main function to start the program
if __name__ == "__main__":
    main()
