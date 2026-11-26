def calculate_subtotal(items: list[tuple[str, float, int]]) -> float:
    subtotal = 0
    for name, price, qty in items:
        subtotal += price * qty
    return subtotal


def calculate_discount(subtotal: float) -> float:
    if subtotal >= 50:
        return subtotal * 0.10
    return 0


def calculate_tax(amount: float) -> float:
    return amount * 0.08


def calculate_tip(amount: float, tip_rate: float) -> float:
    return amount * tip_rate


def calculate_bill(
    items: list[tuple[str, float, int]],
    tip_rate: float,
) -> dict[str, float]:
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    tax = calculate_tax(subtotal)
    tip = calculate_tip(subtotal - discount, tip_rate)
    total = round(subtotal - discount + tax + tip, 2)

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "tip": tip,
        "total": total,
    }