def main():
    import argparse
    from reverse_string import reverse_string
    from palindrome_checker import is_palindrome
    from swap_numbers import number_swapped
    from check_odd_even import odd_even
    from largest_three_num import largest_num

    parser = argparse.ArgumentParser(description="Modular Python App")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for reversing a string
    reverse_parser = subparsers.add_parser('reverse', help='Reverse a string')
    reverse_parser.add_argument('string', type=str, help='String to reverse')

    # Subparser for checking palindrome
    palindrome_parser = subparsers.add_parser('palindrome', help='Check if a string is a palindrome')
    palindrome_parser.add_argument('string', type=str, help='String to check')

    # Subparser for Swapping numbers
    swap_parser = subparsers.add_parser('swap', help='Swap two numbers')
    swap_parser.add_argument('number1', type=int, help='This is first number')
    swap_parser.add_argument('number2', type=int, help='This is second number')

    # Subparser for largest of three numbers
    largest_parser = subparsers.add_parser('largest', help='Find the largest of three numbers')
    largest_parser.add_argument('number1', type=int, help='First number')
    largest_parser.add_argument('number2', type=int, help='Second number')
    largest_parser.add_argument('number3', type=int, help='Third number')

    # Subparser for odd/even check
    odd_even_parser = subparsers.add_parser('odd_even', help='Check if a number is odd or even')
    odd_even_parser.add_argument('number', type=int, help='The number to check')

    args = parser.parse_args()

    if args.command == 'reverse':
        result = reverse_string(args.string)
        print(f'Reversed string: {result}')
    elif args.command == 'palindrome':
        result = is_palindrome(args.string)
        print(f'Is palindrome: {result}')
    elif args.command == 'swap':
        result = number_swapped(args.number1, args.number2)
        print(f'Swapped numbers: {result}')
    elif args.command == 'odd_even':
        result = odd_even(args.number)
        print(f'The number {args.number} is {"even" if result else "odd"}.')
    elif args.command == 'largest':
        result = largest_num(args.number1, args.number2, args.number3)
        print(f'The largest number is: {result}')
    else:
        parser.print_help()

if __name__ == "__main__":
    main()