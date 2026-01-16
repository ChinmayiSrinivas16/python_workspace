try:
    num=int(input("enter num:"))
    print("execeution started.......")
    print(10/num)
    print("phase1 completed")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")