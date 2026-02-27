def months_to_down_payment(
    total_cost,
    portion_down_payment,
    annual_salary,
    portion_saved,
    r 
):
    """
    Calculate the number of months required to save for a down payment on a house.
    
    Arguments: 
        total_cost (float): The total cost of the house.
        portion_down_payment (float): The portion of the total cost that is the down payment.
        annual_salary (float): The annual salary of the user.
        portion_saved (float): The portion of the monthly salary that is saved.
        r (float): The annual return rate on savings/investments.

    Returns:
        int: The number of months required to save for the down payment.
    """

    # -- Guardrail -- Ensures that the inputs are valid
    if r < 0 or r > 15:
        raise ValueError("Annual return rate must be between 0% and 15%.")
    
    # -- Core Logic -- 
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment

    current_savings = 0.0
    months = 0

    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)  # Add monthly return on current savings
        current_savings += monthly_salary * portion_saved  # Add monthly savings from salary
        months += 1
    
    return months


def required_savings_rate(
    total_cost,
    portion_down_payment,
    annual_salary,
    monthly_goal,
    r
):
    """
    Calculate the required monthly savings rate (as a decimal) needed to reach the down payment goal within a specified number of months.

    Arguments:
        total_cost (float): The total cost of the house.
        portion_down_payment (float): The portion of the total cost that is the down payment.
        annual_salary (float): The annual salary of the user.
        monthly_goal (int): The number of months within which to save for the down payment.
        r (float): The annual return rate on savings/investments.
    
    Returns:
        float: The required monthly savings rate (as a decimal; 0.125 = 12.5%) to reach the down payment goal.
    """

    # -- Guardrail -- Ensures that the inputs are valid
    if monthly_goal <= 0:
        raise ValueError("Monthly goal must be greater than zero.")
    if portion_down_payment <= 0 or portion_down_payment > 1:
        raise ValueError("Down payment portion must be between 0 and 1 (input as a decimal for accurate calculation).")
    if annual_salary <= 0:
        raise ValueError("Annual salary must be greater than zero.")
    if r < 0:
        raise ValueError("Annual return rate cannot be negative.")

    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary / 12

    low = 0.0
    high = 1.0
    epsilon = 0.0001
    guess = (high + low) / 2.0

    while True:
        current_savings = 0.0
        for month in range(monthly_goal):
            current_savings += current_savings * (r / 12)  # Add monthly return on current savings
            current_savings += monthly_salary * guess  # Add monthly savings from salary
        if abs(current_savings - down_payment) <= epsilon:
            break
        if current_savings < down_payment:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0

    return guess

choice = input("Choose a calculation: (1) Months to Down Payment, (2) Required Savings Rate: ").strip()

if choice == '1':
    total_cost = float(input("Enter the total cost of the house: "))
    portion_down_payment = float(input("Enter the portion of the total cost for the down payment (as a decimal, e.g., 0.25 for 25%): "))
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion of your monthly salary to save (as a decimal, e.g., 0.1 for 10%): "))
    r = float(input("Enter the annual return rate on savings/investments (as a percentage, e.g., 5 for 5%): "))

    months = months_to_down_payment(total_cost, portion_down_payment, annual_salary, portion_saved, r)
    print(f"You will need {months} months to save for the down payment.")
elif choice == '2':
    total_cost = float(input("Enter the total cost of the house: "))
    portion_down_payment = float(input("Enter the portion of the total cost for the down payment (as a decimal, e.g., 0.25 for 25%): "))
    annual_salary = float(input("Enter your annual salary: "))
    monthly_goal = int(input("Enter the number of months to save for the down payment: "))
    r = float(input("Enter the annual return rate on savings/investments (as a percentage, e.g., 0.05 for 5%): "))

    savings_percentage = required_savings_rate(total_cost, portion_down_payment, annual_salary, monthly_goal, r)
    print(f"You need to save {savings_percentage:.2f} or {savings_percentage*100:.2f}% of your monthly salary to reach your down payment goal in {monthly_goal} months.")
else:
    print("Invalid selection. Please restart and choose either 1 or 2.")