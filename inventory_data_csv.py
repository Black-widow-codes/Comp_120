import csv

# Open and read the CSV file
with open("inventory_data.csv", newline="") as f:
    rows = csv.DictReader(f)

    # Print header
    print("Items Needing Reorder:")
    print("-" * 50)
    print(f"{'Product ID':<15} {'Category':<20}")
    print("-" * 50)

    # Iterate through each row and check if stock is below reorder threshold
    items_needing_reorder = []
    for row in rows:
        # Parse stock_level, handling edge cases
        stock_text = row["stock_level"].strip()
        if stock_text.isdigit():
            stock = int(stock_text)
        else:
            # Handle "Out of Stock" or empty values as 0
            stock = 0

        # Parse reorder_threshold
        threshold = int(row["reorder_threshold"])

        # Check if stock is below threshold
        if stock < threshold:
            items_needing_reorder.append({
                "product_id": row["product_id"],
                "category": row["category"],
                "stock": stock,
                "threshold": threshold
            })

    # Print items needing reorder
    if items_needing_reorder:
        for item in items_needing_reorder:
            print(f"{item['product_id']:<15} {item['category']:<20}")
    else:
        print("No items need reordering.")

    print("-" * 50)
    print(f"Total items needing reorder: {len(items_needing_reorder)}")
