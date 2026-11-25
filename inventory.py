def average_price(items):
    return sum(item["price"] for item in items) / len(items)


def find_item(items, sku):
    for item in items:
        if item["sku"] == sku:
            return item
    return None


def restock(stock, sku, qty):
    stock[sku] = stock.get(sku, 0) + qty
    return stock[sku]
