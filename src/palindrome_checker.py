def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check if a string is a palindrome.")
    parser.add_argument("string", type=str, help="The string to check.")
    args = parser.parse_args()

    if is_palindrome(args.string):
        print(f'"{args.string}" is a palindrome.')
    else:
        print(f'"{args.string}" is not a palindrome.')