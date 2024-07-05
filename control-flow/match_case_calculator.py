#!/usr/bin/env python3


def main ():

    try:
            num1 = float (input('Enter the first number:'))
            num2 = float (input('enter the second number:'))
    except  ValueError:
          print('Invalid input.Please entr numeric values.')
          return
    operation = input('Choose the operaration (+, -, *, ?):')

    match operation:
        case '+':
                result = num1 + num2
                print(f'The result is {result}.')
        case '-':
                result = num1 - num2
                print(f'The result is {result}.')
        case '*':
                result = num1 * num2
                print(f'The result is {result}.')
        case "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose one of +, -, *, /.")

if __name__ == "__main__":
    main()
            