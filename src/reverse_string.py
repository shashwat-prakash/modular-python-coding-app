def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Reverse a string.")
    parser.add_argument("string", type=str, help="The string to reverse.")
    args = parser.parse_args()

    reversed_str = reverse_string(args.string)
    print(f"Reversed string: {reversed_str}")