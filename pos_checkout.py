"""Campus retail point-of-sale checkout."""

from decimal import Decimal
import math


def prompt_item_name() -> str:
    while True:
        name = input("Item name (or DONE to finish): ").strip()
        if name:
            return name
        print("Item name cannot be empty.")


def prompt_unit_price() -> float:
    while True:
        try:
            price = float(input("Unit price: ").strip())
            if math.isfinite(price) and price > 0:
                return price
        except ValueError:
            pass
        print("Enter a valid price greater than 0.")


def prompt_quantity() -> int:
    while True:
        try:
            quantity = int(input("Quantity: ").strip())
            if quantity >= 1:
                return quantity
        except ValueError:
            pass
        print("Enter a whole-number quantity of at least 1.")


def main() -> None:
    student_key = input("Student key: ")
    seed = sum(ord(ch) for ch in student_key.strip())

    subtotal = Decimal("0")
    units = 0

    while True:
        item_name = prompt_item_name()
        if item_name == "DONE":
            break

        unit_price = prompt_unit_price()
        quantity = prompt_quantity()

        subtotal += Decimal(str(unit_price)) * quantity
        units += quantity

    discount_percent = 10 if units >= 10 or subtotal >= Decimal("100") else 0
    discount = subtotal * Decimal(discount_percent) / Decimal("100")
    total = subtotal - discount
    perk_applied = seed % 2 == 1

    if perk_applied:
        total = max(Decimal("0"), total - Decimal("3.00"))

    print(f"Seed: {seed}")
    print(f"Units: {units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
