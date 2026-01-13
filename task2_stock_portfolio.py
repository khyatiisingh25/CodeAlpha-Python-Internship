# Stock Portfolio Tracker
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}
total_value = 0
print("Simple Stock Portfolio Tracker")
print("Available stocks and prices:")
print(stocks)
choice = "yes"
while choice == "yes":
    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    if name in stocks:
        value = stocks[name] * quantity
        total_value = total_value + value
        print("Value of this stock:", value)
    else:
        print("Stock not available")
    choice = input("Do you want to add more stocks? (yes/no): ")
print("\nTotal Investment Value:", total_value)
