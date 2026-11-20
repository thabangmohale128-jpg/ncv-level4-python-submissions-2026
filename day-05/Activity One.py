class Product:
    VAT_RATE = 0.15

    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"{self.code} - {self.name}: "
                f"R{self.price:.2f}, Quantity: {self.quantity}")

    def calc_vat(self):
        return self.price * self.VAT_RATE

    def price_including_vat(self):
        return self.price + self.calc_vat()

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        return self.price - discount

    def total_value(self):
        return self.price * self.quantity


def main():
    product1 = Product("P001", "Keyboard", 450.00, 10)
    product2 = Product("P002", "Mouse", 250.00, 20)

    print(product1)
    print(product2)

    print("\nVAT:", product1.calc_vat())
    print("Price including VAT:", product1.price_including_vat())
    print("Price after 10% discount:", product1.apply_discount(10))
    print("Total stock value:", product1.total_value())

    print("\nVAT:", product2.calc_vat())
    print("Price including VAT:", product2.price_including_vat())
    print("Price after 10% discount:", product2.apply_discount(10))
    print("Total stock value:", product2.total_value())


main()