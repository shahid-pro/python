
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Construct lines
# x > 0
d = np.linspace(-2,16,300)
x,y = np.meshgrid(d,d)
plt.imshow( ((3*y <= (12-2*x)) & (y <= (3+x)) & (x <= 4) & (y>=3)).astype(int) ,
                extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

x = np.linspace(0, 20, 2000)
y = np.linspace(0, 20, 2000)


y1 = (12-2*x)/3

y2 = (3+x)

x1 = (y*0) + 4

y3 = (x*0) + 3

# Make plot
plt.plot(x, y1, label=r'C1')
plt.plot(x, y2, label=r'C2')
plt.plot(x1, y, label=r'C3')
plt.plot(x, y3, label=r'C4')

plt.xlim((0, 16))
plt.ylim((0, 11))
plt.xlabel('x')
plt.ylabel('y')
# Fill feasible region
# y5 = np.minimum(y2, y4)
# y6 = np.maximum(y1, y3)
# plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)



# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize)

# Create problem Variables
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0

# Objective Function
Lp_prob += 3 * x + 5 * y

# Constraints:
Lp_prob += 2 * x + 3 * y <= 12
Lp_prob += -x + y <= 3
Lp_prob += x <= 4
Lp_prob += y >= 3

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))

# importing library sympy
from sympy import symbols, Eq, solve

# defining symbols used in equations
# or unknown variables
x, y = symbols('x,y')

# defining equations
eq1 = Eq((2*x+3*y), 12)
print("Equation 1:")
print(eq1)
eq2 = Eq((x), 4)
print("Equation 2")
print(eq2)

# solving the equation
print("Values of 2 unknown variable are as follows:")

print(solve((eq1, eq2), (x, y)))

x = np.linspace(-5, 5, 2000)
y = np.linspace(-5, 5, 2000)


y1 = (12-2*x)/3


x1 = (y*0) + 4


# Make plot
plt.plot(x, y1, label=r'C1')
plt.plot(x1, y, label=r'C2')