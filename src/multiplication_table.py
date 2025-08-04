def multiplication_table(n):
    """Generate a multiplication table for the given number."""
    table = []
    for i in range(1,11):
        num = n * i
        table.append(f"{n} * {i} = {num} \n")
    return table

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Check if a number is odd or even.")
    parser.add_argument("number", type=int, help="The number to check.")
    args = parser.parse_args()

    