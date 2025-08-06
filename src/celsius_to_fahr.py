def convert_celsius_to_fahr(celsius):
    """Convert Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")

    return (celsius * 9/5) + 32

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit')
    parser.add_argument('celsius', type=float, help='Temperature in Celsius to convert')
    args = parser.parse_args()

    fahrenheit = convert_celsius_to_fahr(args.celsius)
    print(f'{args.celsius} Celsius is {fahrenheit} Fahrenheit')

