# format_invoice.py 
import datetime

subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print(
    "Sub: ${0} Tax: ${1} Total: ${total}".format(
    subtotal, tax, total=total
    )
) 

print(
    "Sub: ${0:0.2f} Tax: ${1:0.2f} "
    "Total: ${total:0.2f}".format(subtotal, tax, total=total)
)

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]
print("PRODUCT    QUANTITY PRICE    SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
    f"{product:10s}{quantity: ^9d} "
    f"${price: <8.2f}${subtotal: >7.2f}"
    )

print("Date {the_date:%Y-%m-%d %I:%M%p }".format(
        the_date=datetime.datetime.now())) 
