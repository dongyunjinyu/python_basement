import sympy as sym
""" 解一阶常微分方程 """
f = sym.symbols('f', cls=sym.Function)  # 定义函数标识符
x = sym.symbols('x')  # 定义变量
eq = sym.Eq(sym.diff(f(x), x, 1), x)  # 构造等式，即dy/dx=y
# diff(函数,自变量,求导次数)
print(sym.dsolve(eq, f(x)))
print('#######################')
sym.pprint(sym.dsolve(eq, f(x)))  # 以"pretty"形式打印方程的解
