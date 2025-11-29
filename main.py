# Helper functions
def ask_amount(message):
    return float(input(message))

def money(amount):
    return f"{amount:,.2f}"

# Incomes
troy_income = ask_amount("Enter Troy's paycheck: ")
partner_income = ask_amount("Enter GF's paycheck: ")
total_income = troy_income + partner_income

# Expenses
rent = ask_amount("Enter the rent: ")
electric = ask_amount("Enter electricity charge: ")

troy_phone = ask_amount("Enter Troy's phone bill: ")
partner_phone = ask_amount("Enter GF's phone bill: ")

groceries = ask_amount("Enter groceries: ")

loan1 = ask_amount("Enter the first loan payment: ")
loan2 = ask_amount("Enter the second loan payment: ")

# Fixed expenses
chiropractor = 20
car_wash = 25
yt_music = 10.99 *2

# Calculations
remaining = total_income
remaining -= rent
remaining -= electric
remaining -= (troy_phone + partner_phone)
remaining -= groceries
remaining -= (loan1 + loan2)
remaining -= yt_music
remaining -= chiropractor
remaining -= car_wash

print(f"After all expenses paid, there is ${money(remaining)} left.")
