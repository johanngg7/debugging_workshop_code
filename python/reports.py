
def find_product_by_name(products, name):
    for product in products:
        if product["name"].lower().strip() == name.lower().strip(): # Should strip the whitespace from '  keyboard  '
            return product
            
    return None


def low_stock_products(products, threshold=5):
    return [p for p in products if p["stock"] < threshold and p["stock"] >= 0] # Should also include stock that is equal to zero


def products_sorted_by_price(products):
    products.sort(key=lambda p: p["price"]) # Should be sorted by price!
    return products


def category_summary(products):
    summary = {}

    for product in products:
        category = product["category"]

        if category not in summary:
            summary[category] = {"product_count": 0, "total_stock": 0}

        summary[category]["product_count"] += product["stock"]
        if product["stock"] > 0: # Should only count products that have an actual stock
            summary[category]["total_stock"] += 1

    return summary


def revenue_summary(processed_orders):
    total_revenue = 0
    valid_orders = 0

    for order in processed_orders: # should iterate through entire list
        if order["valid"]:
            valid_orders += 1
            total_revenue += order["subtotal"]

    return {
        "valid_orders": valid_orders,
        "total_revenue": round(total_revenue, 2),
    }
