#!/usr/bin/env python3

# multiplication_table.py

def main():
    # Prompt user for a number
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    # Generate and print the multiplication table
    for i in range(1, 10 + 1):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()