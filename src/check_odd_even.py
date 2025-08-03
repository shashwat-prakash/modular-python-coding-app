def odd_even(num):
    """Check if a number is odd or even."""
    return num % 2 == 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Check if a number is odd or even.")
    parser.add_argument("number", type=int, help="The number to check.")
    args = parser.parse_args()

    is_even = odd_even(args.number)
    if is_even:
        print(f"The number {args.number} is even.")
    else:
        print(f"The number {args.number} is odd.")