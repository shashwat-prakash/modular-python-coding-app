def largest_num(num1, num2, num3):
    #return max(num1, num2, num3)
    
    # without using max function
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Check if a number is odd or even.")
    parser.add_argument("number", type=int, help="The number to check.")
    args = parser.parse_args()

    is_even = largest_num(args.number1, args.number2, args.number3)

