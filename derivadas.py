import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Defino a la variable "X"
x = sp.symbols('x')

# Defino a mi función matemática asociada a la variable "X"
f = x**2+3*x+2
print(f)
sp.pretty_print(f)
print('''Con el comando "sp.pretty_print()" hago a la expresión de una función
matemáticamucho mas linda y amigable hacia el ser humano''')

# Defino la derivada de la función "f" usando el método "limit"
h = sp.symbols('h')
f_limit = sp.limit((f.subs(x,x+h)-f)/h,h,0)
sp.pretty_print(f_limit)

# Cálculo la derivada de la función "f" usando el método "diff"
f_prime_diff = sp.diff(f,x)
sp.pretty_print(f_prime_diff)

# Voy a convertir las funciones simbólicas a funciones numéricas para poder evaluarlas y no tener ningún inconveniente
f_lambdified = sp.lambdify(x,f,'numpy')
f_prime_limit_lambdified = sp.lambdify(x,f_limit,'numpy')
f_prime_diff_lambdified = sp.lambdify(x,f_prime_diff,'numpy')
x_vals = np.linspace(-10,10,400)
y_vals = f_lambdified(x_vals)
y_prime_limit_vals = f_prime_limit_lambdified(x_vals)
y_prime_diff_vals = f_prime_diff_lambdified(x_vals)

# Vamos a graficar la función y su derivada
plt.figure(figsize=(10,6))
plt.plot(x_vals,y_vals,label=r'$f(x)=x**2+3*x+2',color='blue')
plt.plot(x_vals,y_prime_limit_vals,label=r'Derivada por definición',color='red',linestyle='--')
plt.plot(x_vals,y_prime_diff_vals,label=r'Derivada con "diff"',color='green',linestyle='-.')
plt.title('Función y sus derivadas')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()