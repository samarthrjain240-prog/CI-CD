
def calculate_total(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    discount = 0.10 * amount if amount > 300 else 0
    discounted_amount = amount - discount
    gst = 0.05 * discounted_amount

    return round(discounted_amount + gst, 2)
