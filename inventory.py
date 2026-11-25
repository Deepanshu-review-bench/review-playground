def average_price(items):
    if not items:
        return 0.0
    return sum(item["price"] for item in items) / len(items)


def find_item(items, sku):
    for item in items:
        if item["sku"] == sku:
            return item
    return None


def restock(stock, sku, qty):
    if qty <= 0:
        raise ValueError("qty must be positive")
    stock[sku] = stock.get(sku, 0) + qty
    return stock[sku]
