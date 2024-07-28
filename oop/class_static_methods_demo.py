#!/usr/bin/env python3
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage:
print(Calculator.add(10, 5))  # Output: 13
print(Calculator.multiply(5, 6))  # Output: Calculation Type: Arithmetic Operations, 30
