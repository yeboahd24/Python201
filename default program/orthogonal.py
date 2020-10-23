#!usr/bin/env/python3
# Orthogonal in software is where by one change in the other part does not affect the other


def calculate_price(base_price: float, tax: float, discount: float) -> float:
    return (base_price * (1 + tax)) * (1 - discount)


def show_price(price: float) -> str:
    return "$ {0:,.2f}".format(price)


def str_final_price(base_price: float, tax: float, discount: float, fmt_function=str) -> str:
    return fmt_function(calculate_price(base_price, tax, discount))


print(str_final_price(10, 0.2, 0.5))
print(str_final_price(1000, 0.2, 0.1, fmt_function=show_price))
