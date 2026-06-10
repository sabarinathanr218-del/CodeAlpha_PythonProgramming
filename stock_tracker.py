stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

total = 0

stock_name = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment Value:", total)
else:
    print("Stock not found")