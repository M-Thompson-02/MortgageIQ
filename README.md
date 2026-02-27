# Housing-Calculator
A python program that helps users calculate:
1. The number of months needed to save for a down payment on a home the user is interested in.
2. The percentage of the user's monthly income that they'll need to save in order to reach their down payment goal in x amount of months. 

## Table of Contents
- [Features] (#features)
- [Installation] (#installation)
- [Usage] (#usage)
- [Functionality] (#functionality)

## Features
- Users can choose between two different calculations:
  1. Number of months needed to reach a down payment.
  2. The percentage of savings required to reach a down payment goal within a set number of months.
- Supports whole numbers and decimals for the first calculation and since the second calculation gives more detailed information the user will need to input decimals in order to get an accurate calculation.
- Both calculations account for the annual rate of return on the user's savings/investments.
- Handles invalid input with guardrails
- Clear output for both calculations
- Both calculation methods are demonstrated and tested within the Jupyter Notebook.

## Installation
1. Clone this repository:
   ''' bash
   git clone https://github.com/monicastaten13-ux/Housing-Calculator.git
2. cd Housing-Calculator
3. jupyter notebook Housing-Calculator.ipynb

## Usage
### Running the code in Jupyter Notebook ('.ipynb')

The notebook is designed to be ran interactively.

1. Open "Housing-Calculator.ipynb"
2. Select "Restart the kernels and run all cells."
3. Follow the prompts for the user input.
4. Once the input is collected the appropriate calculation will display at the very bottom of the notebook. 

### Running the Python script ('.py')

The Python script runs the same calculations without the notebook interface. The Python script can be ran in Visual Studio Code. 

1. Install Python (https://www.python.org/downloads/)
2. Install Visual Studio Code
3. Clone this repository or download the ZIP
4. Open the project folder in VS Code
5. Open "housing_calculator.py"
6. Run the file using:
   '''bash
   python housing_calculator.py

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
