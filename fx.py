def convert(amount, from_currency, to_currency, rate):
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if rate <= 0:
        raise ValueError("rate must be positive")
    if from_currency == to_currency:
        return float(amount)
    return float(amount) * rate
