import random

def generate_minutes():
    return random.randint(30, 180)

def calculate_amount(machine_type, minutes):
    hours = minutes / 60
    if machine_type == "A":
        initial = 50.00
        rate = 30.00
    elif machine_type == "B":
        initial = 62.50
        rate = 36.25
    else:
        initial = 74.87
        rate = 40.50
    amount = initial + (rate * hours)
    return amount


def calculate_total_amount(amount):
    vat = amount * 0.14
    total = amount + vat
    return vat, total

def display_summary(payments):
    customers = len(payments)
    total = sum(payments)
    average = total / customers
    highest = max(payments)
    lowest = min(payments)

    print("\nDAILY SUMMARY")
    print("Customers:", customers)
    print("Total Payments: R", format(total, ".2f"))
    print("Average Payment: R", format(average, ".2f"))
    print("Highest Payment: R", format(highest, ".2f"))
    print("Lowest Payment: R", format(lowest, ".2f"))

def process_payments():
    num_customers = int(input("How many customers? "))
    payments = []
    for count in range(num_customers):
        print("\nCustomer", count + 1)
        name = input("Enter name: ")
        machine = input("Enter machine type (A/B/C): ")
        minutes = generate_minutes()
        amount = calculate_amount(machine, minutes)
        vat, total = calculate_total_amount(amount)
        payments.append(total)

        print("\nINVOICE")
        print("Name:", name)
        print("Machine:", machine)
        print("Minutes Used:", minutes)
        print("Amount Before VAT: R", format(amount, ".2f"))
        print("VAT: R", format(vat, ".2f"))
        print("Total Payable: R", format(total, ".2f"))

    display_summary(payments)


process_payments()