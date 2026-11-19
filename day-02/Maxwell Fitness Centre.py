# Program to calculate customer payments
def amount_due(facility_code, hours):
    if facility_code == "squa":
        rate = 13.00
    elif facility_code == "swim":
        rate = 12.00
    elif facility_code == "gym":
        rate = 11.00
    elif facility_code == "wei":
        rate = 8.00
    amount = rate * hours
    return amount

def final_amount_due(amount):
    vat = amount * 0.14
    final_amount = amount + vat
    return final_amount

def display(name, final_amount):
    print("\n------ MAXWELL FITNESS CENTRE ------")
    print("Customer name:", name)
    print("Final amount payable: R", format(final_amount, ".2f"))
    print("------------------------------------")

def process_payment():

    # Get customer details
    name = input("Enter customer name: ")

    print("\nAvailable Facilities:")
    print("squa - Squash court (R13.00 per hour)")
    print("swim - Swimming pool (R12.00 per hour)")
    print("gym  - Gymnasium (R11.00 per hour)")
    print("wei  - Weights (R8.00 per hour)")

    facility_code = input("\nEnter facility code: ").lower()

    hours = float(input("Enter number of hours: "))

    # Calculate amount before VAT
    amount = amount_due(facility_code, hours)

    # Calculate final amount including VAT
    final_amount = final_amount_due(amount)

    # Display final payment
    display(name, final_amount)

process_payment()