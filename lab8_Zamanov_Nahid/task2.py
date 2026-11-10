def add_vat(price, vat_percent=18):
    """Return the price with VAT added."""
    return price + price * vat_percent / 100


print(add_vat(100))                      # 118.0
print(add_vat(50, 10))                   # 55.0
print(add_vat(vat_percent=5, price=80))  # 84.0
