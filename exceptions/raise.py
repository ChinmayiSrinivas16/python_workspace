bal=5000

def withdraw_money(amount):
    global bal
    if amount<=0:
        raise ValueError("amount must be greater than zero")
    
    if amount>bal:
        raise RuntimeError("insufficient balance")
    
    bal-=amount
    return bal

try:
    print("welcome to ATM")

    user_input=input("enter the amount: ")
    amount=float(user_input)

    remaining_bal=withdraw_money(amount)
    print(f"withdarw success")
    print(f"remaining bal: ${remaining_bal}")

except ValueError as ve:
    print("Input error: ",ve)
except RuntimeError as re:
    print("Transaction Error:", re)

except Exception as e:
    print("Unexpected Error occurred.")

else:
    print("Transaction completed without errors.")

finally:
    print("\n--- SESSION CLOSED ---")
    print("Thank you for using the ATM!")


