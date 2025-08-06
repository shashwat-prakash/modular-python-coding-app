def num_of_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Count the number of vowels in a string.")
    parser.add_argument("string", type=str, help="The string to count vowels in.")
    args = parser.parse_args()

    counting = num_of_vowels(args.string)
    print(f"Number of vowels in the string: {counting}")
