from sympy import symbols, simplify


def solve(text,expr):
    print(f'{text}:\n{expr}')
    simplified_expr = simplify(expr)
    print(f'SOLVED = {simplified_expr}')
    print("")


a,x  = symbols('a x')
b  = symbols('b')
t  = symbols('t')

# ZAD 1
solve('Zad 1a', (2*a-5)*(3*a+2)-11*(-a+1) )
solve('Zad 1b', -20*x+(3*x+5)*(2*x+3)-15 )
solve('Zad 1c', (t+4)*(2*t-4)-2*(t+1)*t )

# ZAD 2
solve('Zad 2a', (a*b**2+4*b**3) * (a*b-6*a**2) )
# ZAD 3
solve('Zad 3a', -(x+1)*(2*x+3)*(x-4))
# ZAD 6
solve('Zad 6a', (a**2+2*a+2) * (a**2-2*a+2) )



