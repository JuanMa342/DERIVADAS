import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

print("Vamos a ver las derivadas parciales de una función de 2 variables")

# Defino las variables "X" e "Y"
x,y,h = sp.symbols('x y h')

# Defino la función matemática de 2 variables
f_xy = x**2*y+y**3
sp.pretty_print(f_xy)

# Vamos a hacer la derivada parcial de la función "f_xy" con respecto a "X" usando el método "limit"
f_partial_x_limit = sp.limit((f_xy.subs(x,x+h)-f_xy)/h,h,0)
sp.pretty_print(f_partial_x_limit)

# Vamos a hacer la derivada parcial de la función "f_xy" con respecto a "X" usando "diff"
f_partial_x_diff = sp.diff(f_xy,x)
sp.pretty_print(f_partial_x_diff)

# Vamos a hacer la derivada parcial de la función "f_xy" con respecto a "Y" usando "limit"
f_partial_y_limit = sp.limit((f_xy.subs(y,y+h)-f_xy)/h,h,0)
sp.pretty_print(f_partial_y_limit)

# Vamos a hacer la derivada parcial de la función "f_xy" con respecto a "Y" usando "diff"
f_partial_y_diff = sp.diff(f_xy,y)
sp.pretty_print(f_partial_y_diff)