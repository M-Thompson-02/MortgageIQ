# MortgageIQ
MortgageIQ is a Python-based housing affordability calculator that helps users determine:
1. How long it will take to save for a home down payment.
2. The percentage of income required to reach a savings goal within a target timeframe. 

## Run Instantly (no setup required)
👉 https://colab.research.google.com/drive/1rdRPLHRlSEaXfGqrqXCyzfQ5az6r9Mrw?usp=sharing

---

## Example Output
<img width="736" height="196" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/b493ef2e-011d-4f35-aa17-278be82c52fc" />
This is an example output from the first calculation method.

<img width="565" height="199" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/81944638-1b6a-4b8e-8b35-36bca63857e7" />
This is an example output from the second calculation method.

## Features
- Dual calculation modes:
  1. Time required to save for a down payment
  2. Required savings rate to hit a goal timeline
- Handles real-world financial inputs (salary, investment return, etc.)
- Both calculations account for the annual rate of return on the user's savings/investments.
- Handles invalid input with guardrails
- Clear output for both calculations
- Both calculation methods are demonstrated and tested within the Jupyter Notebook.

## Installation
1. Clone this repository:
   ''' bash
   git clone https://github.com/monicastaten13-ux/MortgageIQ.git
2. cd MortgageIQ
3. jupyter notebook MortgageIQ.ipynb

## Usage
### Running the code in Jupyter Notebook ('.ipynb')

The notebook is designed to be ran interactively.

1. Open "MortgageIQ.ipynb"
2. Select "Restart the kernels and run all cells."
3. Follow the prompts for the user input.
4. Once the input is collected the appropriate calculation will display at the very bottom of the notebook. 

### Running the Python script ('.py')

The Python script runs the same calculations without the notebook interface. The Python script can be ran in Visual Studio Code. 

1. Install Python (https://www.python.org/downloads/)
2. Install Visual Studio Code
3. Clone this repository or download the ZIP
4. Open the project folder in VS Code
5. Open "MortgageIQ.py"
6. Run the file using:
   '''bash
   python MortgageIQ.py

## Functionality

The project includes:

1. 'months = months_to_down_payment (total_cost, portion_down_payment, annual_salary, portion_saved, r)'
   - Calculates the months required to save for the down payment including the return on savings/investments.
   - Guardrails prevent negative salaries, invalid rates, and invalid portions.
   - User's input can be a whole number or can be a decimal. Either input will not have an impact on the calculation given back to the user.

2. 'savings_percentage = required_savings_rate (total_cost, portion_down_payment, annual_salary, monthly_goal, r)'
   - Calculates the monthly savings percentage needed to reach a down payment in a given number of months.
   - Guardrails prevents invalid monthly goals, salaries, negative return rates, and a down payment percentage that is less that zero but no higher than one.
   - The savings rate calculation uses an iterative bisection-style approach to efficiently determine the minimum savings percentage required to reach the down payment goal within a specified time frame
   - The function outputs both decimal and percentage formats.

### Notes:
- All of the percentages provided by the user are decimals in the calculations (0.25 = 25%)
- '.strip()' is used to clean up the user input for the menu choices
- All user inputs are validated before calculations
