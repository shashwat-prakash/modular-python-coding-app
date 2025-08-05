def calc_factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    factorial = 0
    for i in range(2, n+1):
        factorial = i * calc_factorial(i-1)
    return factorial
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a factorial to nth number.")
    parser.add_argument("number", type=int, help="The number to Generate a factorial to nth number.")
    args = parser.parse_args()
    
    table = calc_factorial(args.number)
    print("".join(table))