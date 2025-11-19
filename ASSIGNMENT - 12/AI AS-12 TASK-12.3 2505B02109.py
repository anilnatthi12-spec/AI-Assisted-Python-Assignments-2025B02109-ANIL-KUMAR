from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the optimization problem
model = LpProblem("Chocolate_Profit_Maximization", LpMaximize)

# Define decision variables
x = LpVariable("Chocolate_A", lowBound=0, cat='Integer')
y = LpVariable("Chocolate_B", lowBound=0, cat='Integer')

# Add constraints
model += x + y <= 5          # Milk constraint
model += 3*x + 2*y <= 12     # Choco constraint

# Define objective function
model += 6*x + 5*y           # Profit function

# Solve the problem
model.solve()

# Output results
print("Optimal Production Plan:")
print(f"Produce {int(x.value())} units of Chocolate A")
print(f"Produce {int(y.value())} units of Chocolate B")
print(f"Maximum Profit: Rs {int(value(model.objective))}")
