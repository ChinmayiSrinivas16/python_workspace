flavors = ("Vanilla", "Chocolate", "Strawberry")
prices = {"Vanilla": 2.5, "Chocolate": 3.0, "Strawberry": 2.75}
servings = ("Cone", "Cup")
transactions = []

while True:
    print("\n1=Menu 2=Order 3=History 4=Exit")
    choice = input("Choice: ")

    if choice == "1":
        for f in flavors:
            print(f, "-> $", prices[f])
        print("Serving:", ", ".join(servings), "| Toppings +$0.50")

    elif choice == "2":
        flavor = input("Flavor: ").capitalize()
        if flavor not in flavors:
            print("Invalid flavor")
            continue
        serving = input("Serving (Cone/Cup): ").capitalize()
        if serving not in servings:
            print("Invalid serving")
            continue
        toppings = set(input("Toppings (comma separated): ").split(","))
        toppings.discard("")
        total = prices[flavor] + 0.5 * len(toppings)
        sale = {"flavor": flavor, "serving": serving, "toppings": toppings, "total": total}
        transactions.append(sale)
        print("Order:", sale)

    elif choice == "3":
        if not transactions:
            print("No transactions")
        else:
            for t in transactions:
                print(t)

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
