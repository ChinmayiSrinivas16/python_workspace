from leaves import calculate_deduction
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Program started")

def calculate_bonus(role, salary):
    if role == "coder":
        return salary * 0.10
    elif role == "designer":
        return salary * 0.15
    elif role == "manager":
        return salary * 0.05
    else:
        logging.error("Invalid role entered")
        return 0

name = input("Enter name: ")
role = input("Enter role (coder/designer/manager): ").lower()
leaves = int(input("Enter number of leaves: "))
base_salary = int(input("Enter base salary: "))

deduction = calculate_deduction(leaves)
salary_after_deduction = base_salary - deduction
bonus = calculate_bonus(role, salary_after_deduction)
final_salary = salary_after_deduction + bonus

print(f"{name}, Final Salary: {final_salary}")
