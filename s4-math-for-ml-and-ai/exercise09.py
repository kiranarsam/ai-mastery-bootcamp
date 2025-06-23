#calculas for ml #derivatives
# f(x) = x*x
import sympy as sp

x = sp.Symbol('x')

f = x ** 2   # x to the power of 2

derivative = sp.diff(f, x)

print(derivative)


x, y = sp.symbols('x y')
f = x ** 2 + y ** 2
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)
print("grad_x: = ", grad_x)
print("grad_y: = ", grad_y)
