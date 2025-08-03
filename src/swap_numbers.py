def number_swapped(number1, number2):
    return number2, number1

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Swapping of 2 numbers")
    parser.add_argument("number1", type=int, help="This is first number")
    parser.add_argument("number2", type=int, help="This is Second number")

    args = parser.parse_args()

    swapped_numbers = number_swapped(args.number1, args.number2)
    print(f"Swapped numbers: {swapped_numbers}")

