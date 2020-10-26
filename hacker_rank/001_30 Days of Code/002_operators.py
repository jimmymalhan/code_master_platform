# mC = float(input())
# tipPercent = 20
# taxPercent = 8
# tip = mC * 20 / 100
# tax = mC * 8 / 100
# totalCost  = int(mC + tip + tax)
# print(totalCost)

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    totalCost = int(round(meal_cost + tip + tax))
    print(totalCost)
if __name__ == '__main__':
    meal_cost = 12.0
    tip_percent = 20
    tax_percent = 8

    print(solve(meal_cost, tip_percent, tax_percent))
