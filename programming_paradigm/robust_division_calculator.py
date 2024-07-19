def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return 'Error: Division by zero is not allowed.'
        return numerator / denominator
    except ValueError:
        return 'Error: Non-numeric input detected. Please provide numbers only.'
    