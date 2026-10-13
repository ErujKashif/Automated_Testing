def get_discount(premium_customer, unpaid_bills):
    if premium_customer and not unpaid_bills:
        return "Yes"

    return "No"